#!/usr/bin/env python3
import argparse,datetime,json,pathlib,re,urllib.parse,urllib.request
root=pathlib.Path(__file__).resolve().parents[4]
p=argparse.ArgumentParser();p.add_argument('mode',choices=['doctor','drive']);p.add_argument('--out',default='.verification-evidence');a=p.parse_args();out=pathlib.Path(a.out).resolve();out.mkdir(parents=True,exist_ok=True)
r={'mode':a.mode,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'ok':False,'checks':[]}
try:
 src=root/'README.md';assert src.is_file() and src.read_text().startswith('---\n---\n'),'README frontmatter/target mismatch'
 assert (root/'index.md').is_symlink() and (root/'index.md').resolve()==src.resolve(),'Site entry no longer points to README'
 config=(root/'_config.yml').read_text();layout=(root/'_layouts/default.html').read_text();assert 'README.md' in config and 'index.md' in config and '{{ content }}' in layout and '{{ page.title }}' in layout,'Site source contract'
 r['checks'].append({'site_entry':'index.md symlink -> README.md','layout_content_slot':True})
 if a.mode=='drive':
  s=src.read_text();links=re.findall(r'\[([^\]]+)\]\(([^)]+)\)',s);assert len(links)>=200,'Unexpected loss of resource links'
  for label,url in links:
   assert label.strip(),'Empty link label';v=urllib.parse.urlsplit(url);assert v.scheme in ['https','http','mailto'],(label,url)
   if v.scheme in ['https','http']:assert v.netloc and not any(c.isspace() for c in url),(label,url)
  headings=[line[3:].strip() for line in s.splitlines() if line.startswith('## ')]
  for section in ['Books','Community','Project Starter Templates','Libraries','Tools','About']:assert section in headings,'Missing section '+section
  r['checks'].append({'resource_links':len(links),'required_sections':headings,'all_url_shapes_valid':True})
  # Bounded reader journey: open guideline repository and compiler-tool resource.
  # isocpp.org returned HTTP403 in a prior run; that remains an unverified endpoint.
  for name in ['C++ Core Guidelines','Compiler Explorer']:
   url=next(u for label,u in links if label==name)
   req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
   with urllib.request.urlopen(req,timeout=20) as response:
    body=response.read(200000).decode('utf-8','replace');assert response.status==200 and '<title' in body.lower(),'Not a readable HTML resource'
    r['checks'].append({'label':name,'source_url':url,'resolved_url':response.url,'status':response.status,'title':re.search(r'<title[^>]*>(.*?)</title>',body,re.I|re.S).group(1).strip()})
 r['ok']=True
except Exception as e:r['failure']=str(e)
(out/(a.mode+'.json')).write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2));raise SystemExit(0 if r['ok'] else 1)
