// Datos compartidos del mapa: adapta window.MAPA (generado en datos.js) a las estructuras de los prototipos
const CATS=[{k:'puntual',n:'Puntual',r:'< 25 %',min:0,max:25,c:'k1'},{k:'hibrida',n:'Híbrida',r:'25–50 %',min:25,max:50,c:'k2'},{k:'mayoritaria',n:'Mayoritaria',r:'50–75 %',min:50,max:75,c:'k3'},{k:'integral',n:'Integral',r:'> 75 %',min:75,max:101,c:'k4'}];
const ELEMS=['Estructura','Muros','Forjados','Cubierta','Fachada','Acabados interiores'];
const cat=p=>CATS.find(c=>p>=c.min&&p<c.max)||CATS[0];
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const M=window.MAPA||{proyectos:[],autores:[],apuntes:[]};
const img=list=>(list||[]).map(x=>x&&x.imagen).find(Boolean)||'';
const P=M.proyectos.map(x=>({id:x.slug,t:x.titulo,as:x.autores,a:x.autores.join(', '),y:x.anio,city:x.municipio,prov:x.comunidad,ll:[+x.lat,+x.lng],u:x.uso,s:x.sistema,e:x.elementos_madera,p:x.porcentaje_madera,d:x.resumen||'',img:img(x.portada)||img(x.imagenes),x}));
const AUI={};M.autores.forEach(a=>{AUI[a.nombre]={t:a.tipo||'Estudio',c:a.ciudad||'',w:a.web||'',logo:a.logo||''}});
const NOTES=M.apuntes.map(x=>({id:x.slug,tp:x.tema,k:x.tipo,t:x.titulo,d:x.entradilla||'',by:x.autoria||'',y:x.anio||'',x}));
const ROUTES={mapa:['./#mapa','Volver al mapa'],proyectos:['./#proyectos','Volver a proyectos'],todos:['./#todos','Volver a todos los proyectos'],autores:['./#autores','Volver a autores'],'todos-autores':['./#todos-autores','Volver a todos los autores'],madera:['./#madera','Volver a Sobre la madera']};
const projUrl=(id,from)=>'proyecto.html?id='+encodeURIComponent(id)+(from?'&from='+from:'');
const noteUrl=id=>'nota.html?id='+encodeURIComponent(id);
// Fondo de imagen para los huecos .ph; sin imagen se mantiene el rayado de marcador
const phStyle=src=>src?` style="background:var(--color-surface) url('${encodeURI(src)}') center/cover no-repeat"`:'';
// Markdown → HTML (marked + DOMPurify, cargados en la página)
const md=s=>window.marked?DOMPurify.sanitize(marked.parse(s||'')):'<p>'+esc(s)+'</p>';
