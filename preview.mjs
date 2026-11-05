import { createServer } from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.join(here,'site');
const port = Number(process.env.PORT || 4173);
const mime = {'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8','.svg':'image/svg+xml','.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.webp':'image/webp','.txt':'text/plain; charset=utf-8'};
createServer(async (req,res)=>{
  try {
    const pathname = decodeURIComponent(new URL(req.url,'http://localhost').pathname);
    const dest = path.resolve(root, '.'+pathname);
    if(dest!==root && !dest.startsWith(root+path.sep)) {res.writeHead(403);res.end('Forbidden');return;}
    let filepath=dest;
    const info=await stat(filepath).catch(()=>null);
    if(info?.isDirectory()) filepath=path.join(filepath,'index.html');
    const data=await readFile(filepath);
    res.writeHead(200,{'Content-Type':mime[path.extname(filepath)]||'application/octet-stream','Cache-Control':'no-cache'});
    res.end(data);
  } catch {res.writeHead(404,{'Content-Type':'text/plain; charset=utf-8'});res.end('404 - File not found');}
}).listen(port,'127.0.0.1',()=>console.log(`Anteprima pronta: http://localhost:${port}/it/`));
