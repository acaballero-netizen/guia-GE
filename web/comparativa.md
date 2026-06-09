# **Guía de Buenas Prácticas (SÍ vs. NO)**
#### Criterios clave de autoconstrucción para garantizar durabilidad y seguridad
*Proyecto MADERAMEN · UPV / ADSIDEO 2024*

---

Esta sección interactiva reúne de forma sumamente visual los aciertos y errores más comunes en el proceso de autoconstrucción. Un pequeño detalle en la ejecución puede marcar la diferencia entre una vivienda sana y duradera o fallos estructurales graves a medio plazo.

---

## **1. fundación y Elevación**

Evitar que la estructura de madera absorba la humedad constante del suelo tropical y la lluvia de Guinea Ecuatorial.

<table class="comparison-table">
  <thead>
    <tr>
      <th class="th-no">❌ INCORRECTO (NO)</th>
      <th class="th-si">✔️ CORRECTO (SÍ)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="td-no">
        <div class="cell-content">
          <div class="cell-title">Pilar enterrado o pegado al suelo</div>
          <div class="cell-graphic">
            <svg viewBox="0 0 200 160" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; display:block;">
              <!-- Terreno -->
              <rect x="10" y="110" width="180" height="40" fill="#e8e6e0" rx="2" />
              <line x1="10" y1="110" x2="190" y2="110" stroke="#b0b0b0" stroke-width="1.5" />
              <!-- Pilar de madera directo enterrado en hormigón -->
              <rect x="65" y="40" width="30" height="90" fill="#dc2f39" fill-opacity="0.15" stroke="#dc2f39" stroke-width="2" />
              <!-- Hormigón de cimiento directo -->
              <rect x="45" y="100" width="70" height="40" fill="none" stroke="#5a5a5a" stroke-width="1.5" stroke-dasharray="3 3" />
              <!-- Ondas de Humedad -->
              <path d="M68,105 Q72,100 76,105 Q80,110 84,105" fill="none" stroke="#dc2f39" stroke-width="1.5" />
              <path d="M68,90 Q72,85 76,90 Q80,95 84,90" fill="none" stroke="#dc2f39" stroke-width="1.5" />
              <!-- Insectos / Termitas (esquema) -->
              <circle cx="50" cy="115" r="2" fill="#1c1c1c" />
              <circle cx="53" cy="118" r="2" fill="#1c1c1c" />
              <line x1="50" y1="115" x2="65" y2="105" stroke="#dc2f39" stroke-width="1" stroke-dasharray="2 2" />
              <!-- Flechas indicativas -->
              <path d="M125,75 L98,75" fill="none" stroke="#dc2f39" stroke-width="1.5" marker-end="url(#arrow-red)" />
              <text x="130" y="72" font-size="9" font-family="var(--sans)" font-weight="600" fill="#dc2f39">Madera podrida</text>
              <text x="130" y="84" font-size="8.5" font-family="var(--sans)" fill="#5a5a5a">Humedad constante</text>
              <text x="130" y="96" font-size="8.5" font-family="var(--sans)" fill="#5a5a5a">y ataque de termitas</text>
              
              <defs>
                <marker id="arrow-red" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
                  <path d="M0,0 L6,3 L0,6 Z" fill="#dc2f39"/>
                </marker>
              </defs>
            </svg>
          </div>
          <div class="cell-desc">
            <ul>
              <li><strong>Contacto directo:</strong> Enterrar pilares crudos de madera directamente en hormigón o tierra natural.</li>
              <li><strong>Efecto de esponja:</strong> La madera chupa el agua del terreno por capilaridad, pudriéndose en menos de 1 año.</li>
              <li><strong>Acceso libre:</strong> Las termitas construyen túneles directos al pilar sin ser detectadas.</li>
            </ul>
          </div>
        </div>
      </td>
      <td class="td-si">
        <div class="cell-content">
          <div class="cell-title">Zócalo elevado y herraje metálico</div>
          <div class="cell-graphic">
            <svg viewBox="0 0 200 160" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; display:block;">
              <!-- Terreno -->
              <rect x="10" y="110" width="180" height="40" fill="#e8e6e0" rx="2" />
              <line x1="10" y1="110" x2="190" y2="110" stroke="#b0b0b0" stroke-width="1.5" />
              <!-- Zapata enterrada -->
              <rect x="40" y="90" width="60" height="40" fill="#b0b0b0" opacity="0.3" stroke="#b0b0b0" stroke-dasharray="2 2" />
              <!-- Zócalo de bloques -->
              <rect x="50" y="40" width="40" height="70" fill="#ffffff" stroke="#5a5a5a" stroke-width="2" />
              <line x1="50" y1="65" x2="90" y2="65" stroke="#e8e6e0" />
              <line x1="50" y1="90" x2="90" y2="90" stroke="#e8e6e0" />
              <!-- Durmiente de madera -->
              <rect x="45" y="25" width="50" height="15" fill="#e8e6e0" stroke="#1c1c1c" stroke-width="1.5" />
              <!-- Pilar elevado con espacio de ventilación -->
              <rect x="58" y="0" width="24" height="20" fill="#ffffff" stroke="#0F6E56" stroke-width="2" />
              <!-- Herraje en U -->
              <path d="M55,10 L55,25 L85,25 L85,10" fill="none" stroke="#0F6E56" stroke-width="2.5" stroke-linecap="round" />
              <!-- Puntos clave o flechas -->
              <path d="M120,45 L100,25" fill="none" stroke="#0F6E56" stroke-width="1.5" marker-end="url(#arrow-green)" />
              <!-- Textos ilustrativos -->
              <text x="105" y="75" font-size="9.5" font-family="var(--sans)" font-weight="600" fill="#0F6E56">Zócalo &gt; 60 cm</text>
              <text x="105" y="90" font-size="8.5" font-family="var(--sans)" fill="#5a5a5a">Protege de lluvia</text>
              <text x="105" y="102" font-size="8.5" font-family="var(--sans)" fill="#5a5a5a">y salpicaduras</text>
              <text x="110" y="20" font-size="9.5" font-family="var(--sans)" font-weight="600" fill="#0F6E56">Elevado 15 cm</text>
              <text x="110" y="32" font-size="8.5" font-family="var(--sans)" fill="#5a5a5a">Evita capilaridad</text>
              <!-- Marker para flechas -->
              <defs>
                <marker id="arrow-green" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
                  <path d="M0,0 L6,3 L0,6 Z" fill="#0F6E56"/>
                </marker>
              </defs>
            </svg>
          </div>
          <div class="cell-desc">
            <ul>
              <li><strong>Zócalo de bloques:</strong> Elevar el arranque de madera al menos 60 cm sobre el terreno.</li>
              <li><strong>Herraje separador:</strong> Los pilares apoyan sobre herrajes metálicos con holgura ventilada de unos 15 cm.</li>
              <li><strong>Efecto:</strong> El agua no salpica la base del pilar y las termitas no tienen acceso directo oculto.</li>
            </ul>
          </div>
        </div>
      </td>
    </tr>
  </tbody>
</table>

---

## **2. Replanteo y Escuadras**

Garantizar que todas las esquinas formen ángulos de 90° exactos para que la estructura superior encaje perfectamente.

<table class="comparison-table">
  <thead>
    <tr>
      <th class="th-no">❌ INCORRECTO (NO)</th>
      <th class="th-si">✔️ CORRECTO (SÍ)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="td-no">
        <div class="cell-content">
          <div class="cell-title">Replanteo deformado ("a ojo")</div>
          <div class="cell-graphic">
            <svg viewBox="0 0 220 160" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; display:block;">
              <!-- Rombo / Rectángulo deformado -->
              <polygon points="40,25 170,25 150,115 20,115" fill="none" stroke="#dc2f39" stroke-width="2.5" />
              <!-- Diagonales desiguales -->
              <line x1="40" y1="25" x2="150" y2="115" stroke="#dc2f39" stroke-width="1.5" stroke-dasharray="4 2" />
              <line x1="170" y1="25" x2="20" y2="115" stroke="#dc2f39" stroke-width="1.5" stroke-dasharray="4 2" />
              <!-- Medidas desiguales -->
              <text x="80" y="55" font-size="8.5" font-family="var(--sans)" font-weight="600" fill="#dc2f39" transform="rotate(35, 80, 55)">D1 = 14.5 m</text>
              <text x="85" y="100" font-size="8.5" font-family="var(--sans)" font-weight="600" fill="#dc2f39" transform="rotate(-25, 85, 100)">D2 = 17.1 m</text>
              <!-- Leyendas -->
              <text x="165" y="80" font-size="9" font-family="var(--sans)" font-weight="600" fill="#dc2f39">D1 ≠ D2 (Error)</text>
              <text x="165" y="92" font-size="8" font-family="var(--sans)" fill="#5a5a5a">Planta romboidal.</text>
              <text x="165" y="102" font-size="8" font-family="var(--sans)" fill="#5a5a5a">La cercha superior</text>
              <text x="165" y="112" font-size="8" font-family="var(--sans)" fill="#5a5a5a">quedará torcida.</text>
            </svg>
          </div>
          <div class="cell-desc">
            <ul>
              <li><strong>Nivelación descuidada:</strong> No medir diagonales cruzadas o conformarse con estimar los ángulos "a ojo".</li>
              <li><strong>Estructura romboidal:</strong> El edificio quedará descuadrado. Las diagonales difieren por varios centímetros.</li>
              <li><strong>Consecuencias:</strong> Las maderas del techo no apoyarán bien, y las planchas de chapa de zinc quedarán torcidas, provocando goteras.</li>
            </ul>
          </div>
        </div>
      </td>
      <td class="td-si">
        <div class="cell-content">
          <div class="cell-title">Método 3-4-5 y doble diagonal</div>
          <div class="cell-graphic">
            <svg viewBox="0 0 220 160" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; display:block;">
              <!-- Rectángulo perfecto -->
              <rect x="25" y="25" width="130" height="90" fill="none" stroke="#0F6E56" stroke-width="2.5" />
              <!-- Diagonales iguales -->
              <line x1="25" y1="25" x2="155" y2="115" stroke="#0F6E56" stroke-width="1.5" stroke-dasharray="4 2" />
              <line x1="155" y1="25" x2="25" y2="115" stroke="#0F6E56" stroke-width="1.5" stroke-dasharray="4 2" />
              <!-- Medidas -->
              <text x="80" y="55" font-size="8.5" font-family="var(--sans)" font-weight="600" fill="#0F6E56" transform="rotate(30, 80, 55)">D1 = 15.8 m</text>
              <text x="80" y="105" font-size="8.5" font-family="var(--sans)" font-weight="600" fill="#0F6E56" transform="rotate(-30, 80, 105)">D2 = 15.8 m</text>
              <!-- Escuadra -->
              <rect x="25" y="105" width="10" height="10" fill="none" stroke="#0F6E56" stroke-width="1" />
              <circle cx="30" cy="110" r="1.5" fill="#0F6E56" />
              <!-- Leyendas -->
              <text x="165" y="50" font-size="9" font-family="var(--sans)" font-weight="600" fill="#0F6E56">Diagonales</text>
              <text x="165" y="62" font-size="9" font-family="var(--sans)" font-weight="600" fill="#0F6E56">Idénticas</text>
              <text x="165" y="74" font-size="8" font-family="var(--sans)" fill="#5a5a5a">Ángulos de</text>
              <text x="165" y="84" font-size="8" font-family="var(--sans)" fill="#5a5a5a">90° perfectos</text>
            </svg>
          </div>
          <div class="cell-desc">
            <ul>
              <li><strong>Control por diagonales:</strong> Medir las dos líneas cruzadas entre esquinas opuestas de la casa.</li>
              <li><strong>Resultado idéntico:</strong> Si la distancia D1 y D2 mide exactamente lo mismo, la planta es un rectángulo perfecto.</li>
              <li><strong>Ensamble fluido:</strong> Las cerchas y las tablas de cerramiento encajarán sin holguras ni deformaciones.</li>
            </ul>
          </div>
        </div>
      </td>
    </tr>
  </tbody>
</table>

---

## **3. Hormigonado y Curado**

Conseguir que el hormigón alcance el 100% de su resistencia mecánica e impedir grietas profundas debidas a la pérdida de agua.

<table class="comparison-table">
  <thead>
    <tr>
      <th class="th-no">❌ INCORRECTO (NO)</th>
      <th class="th-si">✔️ CORRECTO (SÍ)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="td-no">
        <div class="cell-content">
          <div class="cell-title">Secado directo bajo el sol</div>
          <div class="cell-graphic">
            <svg viewBox="0 0 200 160" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; display:block;">
              <!-- Bloque hormigón zapata agrietado -->
              <rect x="30" y="80" width="140" height="50" fill="#ffffff" stroke="#dc2f39" stroke-width="2.5" />
              <!-- Sol abrazador -->
              <circle cx="170" cy="30" r="12" fill="none" stroke="#dc2f39" stroke-width="2.5" />
              <line x1="170" y1="12" x2="170" y2="4" stroke="#dc2f39" stroke-width="2" />
              <line x1="170" y1="48" x2="170" y2="56" stroke="#dc2f39" stroke-width="2" />
              <line x1="152" y1="30" x2="144" y2="30" stroke="#dc2f39" stroke-width="2" />
              <line x1="188" y1="30" x2="196" y2="30" stroke="#dc2f39" stroke-width="2" />
              <!-- Grietas en el hormigón -->
              <path d="M70,80 L75,95 L72,110" fill="none" stroke="#dc2f39" stroke-width="2" />
              <path d="M120,80 L118,92 L125,105" fill="none" stroke="#dc2f39" stroke-width="2" />
              <!-- Textos -->
              <text x="35" y="25" font-size="9" font-family="var(--sans)" font-weight="600" fill="#dc2f39">Sol ecuatorial abrasador</text>
              <text x="35" y="37" font-size="8" font-family="var(--sans)" fill="#5a5a5a">Evaporación rápida del agua.</text>
              <text x="45" y="123" font-size="9" font-family="var(--sans)" font-weight="600" fill="#dc2f39">Grietas de retracción</text>
              <text x="30" y="148" font-size="9" font-family="var(--sans)" fill="#5a5a5a">Resistencia reducida a la mitad.</text>
            </svg>
          </div>
          <div class="cell-desc">
            <ul>
              <li><strong>Secado al aire:</strong> Dejar el hormigón recién vertido expuesto directamente al sol intenso y el calor.</li>
              <li><strong>Evaporación exprés:</strong> El sol ecuatorial evapora el agua de amasado antes de que el cemento fragüe.</li>
              <li><strong>Consecuencias:</strong> Aparecen fisuras y grietas profundas. El hormigón queda frágil, polvoriento y quebradizo.</li>
            </ul>
          </div>
        </div>
      </td>
      <td class="td-si">
        <div class="cell-content">
          <div class="cell-title">Curado húmedo constante</div>
          <div class="cell-graphic">
            <svg viewBox="0 0 200 160" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; display:block;">
              <!-- Bloque hormigón zapata -->
              <rect x="30" y="80" width="140" height="50" fill="#ffffff" stroke="#0F6E56" stroke-width="2.5" />
              <!-- Cubierta de sacos húmedos / hojas -->
              <path d="M25,75 Q90,70 175,75 L175,82 Q90,78 25,82 Z" fill="#e8e6e0" stroke="#b0b0b0" stroke-width="1" />
              <!-- Gotas de agua / Humectación -->
              <circle cx="60" cy="50" r="1.5" fill="#0F6E56" />
              <circle cx="100" cy="45" r="1.5" fill="#0F6E56" />
              <circle cx="140" cy="55" r="1.5" fill="#0F6E56" />
              <path d="M60,53 L60,62" stroke="#0F6E56" stroke-width="1.5" stroke-linecap="round" />
              <path d="M100,48 L100,58" stroke="#0F6E56" stroke-width="1.5" stroke-linecap="round" />
              <path d="M140,58 L140,65" stroke="#0F6E56" stroke-width="1.5" stroke-linecap="round" />
              <!-- Textos -->
              <text x="45" y="110" font-size="10" font-family="var(--sans)" font-weight="600" fill="#0F6E56">Curado húmedo (7 días)</text>
              <text x="30" y="148" font-size="9" font-family="var(--sans)" fill="#5a5a5a">Hormigón sano, denso y compacto.</text>
            </svg>
          </div>
          <div class="cell-desc">
            <ul>
              <li><strong>Protección solar:</strong> Cubrir el hormigón fresco con plástico, sacos de tela o grandes hojas de plátano.</li>
              <li><strong>Riego constante:</strong> Regar suavemente con agua limpia 2 o 3 veces al día durante los primeros 7 días.</li>
              <li><strong>Efecto:</strong> El agua necesaria para la reacción química del cemento no se evapora, logrando la máxima dureza.</li>
            </ul>
          </div>
        </div>
      </td>
    </tr>
  </tbody>
</table>

---

## **4. Apoyo de Cerchas**

Garantizar que todo el peso de la cubierta de zinc y la lluvia se transmita directamente al suelo mediante soportes aptos.

<table class="comparison-table">
  <thead>
    <tr>
      <th class="th-no">❌ INCORRECTO (NO)</th>
      <th class="th-si">✔️ CORRECTO (SÍ)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="td-no">
        <div class="cell-content">
          <div class="cell-title">Apoyo en zuncho (viga libre)</div>
          <div class="cell-graphic">
            <svg viewBox="0 0 200 160" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; display:block;">
              <!-- Dos pilares alejados -->
              <rect x="25" y="60" width="20" height="80" fill="#ffffff" stroke="#b0b0b0" stroke-width="1.5" />
              <rect x="155" y="60" width="20" height="80" fill="#ffffff" stroke="#b0b0b0" stroke-width="1.5" />
              <!-- Viga horizontal de atado deformada/flectada -->
              <path d="M25,50 Q100,68 175,50 L175,60 Q100,78 25,60 Z" fill="#ffffff" stroke="#dc2f39" stroke-width="2" />
              <!-- Cercha apoyando en el centro (error) -->
              <polygon points="85,25 100,0 115,0 115,25" fill="#e8e6e0" stroke="#1c1c1c" stroke-width="1.5" />
              <rect x="75" y="25" width="50" height="10" fill="#e8e6e0" stroke="#1c1c1c" stroke-width="1.5" />
              <!-- Flecha de fuerza deformante -->
              <path d="M100,10 L100,55" fill="none" stroke="#dc2f39" stroke-width="2" marker-end="url(#force-red)" />
              <!-- Leyendas -->
              <text x="65" y="100" font-size="9" font-family="var(--sans)" font-weight="600" fill="#dc2f39">Flexión Crítica (¡Peligro!)</text>
              <text x="35" y="115" font-size="8" font-family="var(--sans)" fill="#5a5a5a">La viga horizontal cede y pandea bajo la carga.</text>
              <text x="35" y="125" font-size="8" font-family="var(--sans)" fill="#5a5a5a">Peligro de colapso de la cercha.</text>
              
              <defs>
                <marker id="force-red" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
                  <path d="M0,0 L6,3 L0,6 Z" fill="#dc2f39"/>
                </marker>
              </defs>
            </svg>
          </div>
          <div class="cell-desc">
            <ul>
              <li><strong>Apoyo descentrado:</strong> Apoyar las cerchas sobre el zuncho horizontal de cerramiento en puntos vacíos de pilares.</li>
              <li><strong>Carga flectora:</strong> La viga o zuncho horizontal sufre flexión concentrada en el centro, esfuerzo para el que no está diseñado.</li>
              <li><strong>Consecuencias:</strong> La viga flecta, cede, deforma la fachada y puede colapsar repentinamente con viento fuerte.</li>
            </ul>
          </div>
        </div>
      </td>
      <td class="td-si">
        <div class="cell-content">
          <div class="cell-title">Apoyo directo sobre pilares</div>
          <div class="cell-graphic">
            <svg viewBox="0 0 200 160" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; display:block;">
              <!-- Pilar de madera vertical -->
              <rect x="85" y="45" width="30" height="95" fill="#ffffff" stroke="#0F6E56" stroke-width="2.5" />
              <!-- Tirante horizontal de la cercha -->
              <rect x="40" y="30" width="120" height="15" fill="#e8e6e0" stroke="#1c1c1c" stroke-width="1.5" />
              <!-- Pares inclinados de la cercha -->
              <polygon points="40,30 100,0 115,0 40,45" fill="#e8e6e0" stroke="#1c1c1c" stroke-dasharray="none" />
              <!-- Flecha de fuerza directa por gravedad -->
              <path d="M100,10 L100,80" fill="none" stroke="#0F6E56" stroke-width="3" marker-end="url(#force-green)" />
              <!-- Leyendas -->
              <text x="120" y="60" font-size="9" font-family="var(--sans)" font-weight="600" fill="#0F6E56">Carga directa</text>
              <text x="120" y="72" font-size="8" font-family="var(--sans)" fill="#5a5a5a">Transmisión axial.</text>
              <text x="120" y="82" font-size="8" font-family="var(--sans)" fill="#5a5a5a">Pilar a compresión</text>
              <text x="120" y="92" font-size="8" font-family="var(--sans)" fill="#5a5a5a">sin flexión.</text>
              
              <defs>
                <marker id="force-green" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
                  <path d="M0,0 L6,3 L0,6 Z" fill="#0F6E56"/>
                </marker>
              </defs>
            </svg>
          </div>
          <div class="cell-desc">
            <ul>
              <li><strong>Apoyo estructural correcto:</strong> El extremo del tirante de la cercha apoya de forma exacta en la cabeza del pilar vertical.</li>
              <li><strong>Esfuerzo axial:</strong> El peso presiona verticalmente el pilar a compresión pura, que es donde la madera destaca por su resistencia.</li>
              <li><strong>Efecto:</strong> Estabilidad absoluta a largo plazo, evitando empujes laterales sobre la fachada.</li>
            </ul>
          </div>
        </div>
      </td>
    </tr>
  </tbody>
</table>

---

## **5. Fijación de Cubiertas**

Evitar por completo las filtraciones y goteras de agua de lluvia torrencial a través de los orificios de fijación en la chapa metálica de zinc.

<table class="comparison-table">
  <thead>
    <tr>
      <th class="th-no">❌ INCORRECTO (NO)</th>
      <th class="th-si">✔️ CORRECTO (SÍ)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="td-no">
        <div class="cell-content">
          <div class="cell-title">Fijación en el valle de la chapa</div>
          <div class="cell-graphic">
            <svg viewBox="0 0 200 160" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; display:block;">
              <!-- Chapa de zinc corrugada (sección) -->
              <path d="M10,80 Q25,50 40,80 Q55,110 70,80 Q85,50 100,80 Q115,110 130,80 Q145,50 160,80 Q175,110 190,80" fill="none" stroke="#5a5a5a" stroke-width="2.5" />
              <!-- Rastreles / Madera inferior -->
              <rect x="25" y="88" width="150" height="20" fill="#e8e6e0" stroke="#b0b0b0" stroke-width="1.5" />
              <!-- Tornillo metido en el valle (x = 55) -->
              <rect x="50" y="80" width="10" height="4" fill="#dc2f39" />
              <rect x="53" y="84" width="4" height="20" fill="#dc2f39" />
              <!-- Agua inundando el valle -->
              <path d="M40,78 C50,86 60,86 70,78 L70,90 C60,94 50,94 40,90 Z" fill="#185FA5" fill-opacity="0.3" />
              <!-- Gotera goteando abajo de la chapa -->
              <path d="M55,112 C55,120 52,122 55,128 C58,122 55,120 55,112 Z" fill="#185FA5" />
              <!-- Leyendas -->
              <text x="80" y="32" font-size="9" font-family="var(--sans)" font-weight="600" fill="#dc2f39">Valle = Gotera Segura</text>
              <text x="25" y="142" font-size="9" font-family="var(--sans)" font-weight="600" fill="#dc2f39">El agua corre por el canal de fijación.</text>
              <text x="25" y="152" font-size="8.5" font-family="var(--sans)" fill="#5a5a5a">Oxidación rápida y gotera constante en la madera.</text>
            </svg>
          </div>
          <div class="cell-desc">
            <ul>
              <li><strong>Fijación en el canal:</strong> Colocar tornillos o clavos en la zona más baja de la corruga de zinc.</li>
              <li><strong>Canal de agua:</strong> Toda la escorrentía del tejado pasa precisamente por ese canal de desagüe.</li>
              <li><strong>Consecuencias:</strong> El agua inunda la cabeza del tornillo continuamente, filtrándose al interior de la vivienda y pudriendo el rastrel de madera inferior.</li>
            </ul>
          </div>
        </div>
      </td>
      <td class="td-si">
        <div class="cell-content">
          <div class="cell-title">Fijación en la cresta de la chapa</div>
          <div class="cell-graphic">
            <svg viewBox="0 0 200 160" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; display:block;">
              <!-- Chapa de zinc corrugada (sección) -->
              <path d="M10,80 Q25,50 40,80 Q55,110 70,80 Q85,50 100,80 Q115,110 130,80 Q145,50 160,80 Q175,110 190,80" fill="none" stroke="#5a5a5a" stroke-width="2.5" />
              <!-- Rastreles / Madera inferior -->
              <rect x="25" y="88" width="150" height="20" fill="#e8e6e0" stroke="#b0b0b0" stroke-width="1.5" />
              <!-- Tornillo con arandela en cresta (x = 85) -->
              <!-- Cabeza tornillo -->
              <rect x="80" y="40" width="10" height="4" fill="#0F6E56" />
              <rect x="83" y="44" width="4" height="25" fill="#0F6E56" />
              <!-- Goma de estanqueidad verde -->
              <ellipse cx="85" cy="50" rx="7" ry="2" fill="#0F6E56" />
              <!-- Flechas de escorrentía de agua por los valles -->
              <path d="M40,70 L50,85 L60,92" fill="none" stroke="#185FA5" stroke-width="1.5" marker-end="url(#arrow-blue)" />
              <path d="M130,70 L120,85 L110,92" fill="none" stroke="#185FA5" stroke-width="1.5" marker-end="url(#arrow-blue)" />
              <!-- Textos -->
              <text x="88" y="32" font-size="9" font-family="var(--sans)" font-weight="600" fill="#0F6E56">Cresta (Sin flujo)</text>
              <text x="30" y="130" font-size="9" font-family="var(--sans)" font-weight="600" fill="#0F6E56">El agua corre por los valles lejanos.</text>
              <text x="30" y="142" font-size="8.5" font-family="var(--sans)" fill="#5a5a5a">Orificio seco. Cero riesgo de goteras.</text>
              
              <defs>
                <marker id="arrow-blue" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
                  <path d="M0,0 L5,2.5 L0,5 Z" fill="#185FA5"/>
                </marker>
              </defs>
            </svg>
          </div>
          <div class="cell-desc">
            <ul>
              <li><strong>Fijación en la cresta:</strong> Los tornillos de cabeza hexagonal o clavos de gancho se meten por la parte más alta de la onda.</li>
              <li><strong>Arandela de goma:</strong> Lleva una arandela flexible de neopreno que sella por completo el orificio por presión.</li>
              <li><strong>Efecto:</strong> El agua de lluvia corre por los valles inferiores, por lo que el orificio del tornillo nunca está inundado.</li>
            </ul>
          </div>
        </div>
      </td>
    </tr>
  </tbody>
</table>
