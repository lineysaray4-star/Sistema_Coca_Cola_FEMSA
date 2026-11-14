<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Planta Coca-Cola FEMSA Barranquilla</title>
  <style>
    :root { --bg: #eef1f5; --ink: #1f2933; --line: #e1e5ea; }
    * { box-sizing: border-box; }
    html, body {
      margin: 0; height: 100%;
      font-family: "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background: var(--bg); color: var(--ink);
      overflow: hidden;
    }
    header {
      height: 64px; display: flex; align-items: center; justify-content: center;
      background: #ffffff; border-bottom: 1px solid var(--line);
      font-size: 1.25rem; font-weight: 600; letter-spacing: .3px;
    }
    #visor { width: 100%; height: calc(100% - 64px); position: relative; }
    #visor canvas { display: block; }
    #cargando {
      position: absolute; inset: 0; display: flex; align-items: center;
      justify-content: center; color: #6b7785; font-size: 1rem; background: var(--bg); z-index: 10;
    }

    /* Estilos corregidos para los Hotspots interactivos (Letra blanca y fondo de alta visibilidad) */
    .Hotspot {
      background: #e61c24;
      border: 2px solid #ffffff;
      border-radius: 50%;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.4);
      cursor: pointer;
      height: 14px;
      width: 14px;
      padding: 0;
      position: absolute;
      transform: translate(-50%, -50%);
      transition: transform 0.2s ease, background 0.2s ease;
      z-index: 5;
    }
    .Hotspot:hover {
      transform: translate(-50%, -50%) scale(1.4);
      background: #000000;
    }
    .HotspotAnnotation {
      background: rgba(20, 24, 33, 0.9);
      border-left: 3px solid #e61c24;
      border-radius: 4px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.35);
      color: #ffffff;
      font-size: 11px;
      font-weight: bold;
      padding: 5px 10px;
      position: absolute;
      top: -32px;
      left: 50%;
      transform: translateX(-50%);
      white-space: nowrap;
      pointer-events: none;
    }
  </style>
  <script type="importmap">
    {"imports": {
      "three": "https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js",
      "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/"
    }}
  </script>
</head>
<body>
  <header>🏭 Planta Coca-Cola FEMSA Barranquilla</header>
  <div id="visor">
    <div id="cargando">Cargando modelo y puntos de interés…</div>
    
    <!-- CONTENEDOR DE HOTSPOTS CON COORDENADAS CORREGIDAS -->
    <div id="hotspots-container">
      <div class="Hotspot" data-x="0.285" data-y="0.085" data-z="-0.090"><div class="HotspotAnnotation">Nave L6</div></div>
      <div class="Hotspot" data-x="-0.075" data-y="0.090" data-z="-0.225"><div class="HotspotAnnotation">Ed. Administrativo</div></div>
      <div class="Hotspot" data-x="-0.012" data-y="0.055" data-z="-0.140"><div class="HotspotAnnotation">Preparación Jarabes</div></div>
      <div class="Hotspot" data-x="-0.085" data-y="0.074" data-z="0.070"><div class="HotspotAnnotation">Nave L5</div></div>
      <div class="Hotspot" data-x="0.120" data-y="0.010" data-z="-0.220"><div class="HotspotAnnotation">PTAP</div></div>
      <div class="Hotspot" data-x="0.175" data-y="0.070" data-z="-0.125"><div class="HotspotAnnotation">Maquinaria Auxiliar</div></div>
      <div class="Hotspot" data-x="0.160" data-y="0.073" data-z="-0.050"><div class="HotspotAnnotation">Almacén Materia Prima</div></div>
      <div class="Hotspot" data-x="0.190" data-y="0.034" data-z="0.120"><div class="HotspotAnnotation">Taller de Mantenimiento</div></div>
      <div class="Hotspot" data-x="0.050" data-y="0.061" data-z="0.110"><div class="HotspotAnnotation">Almacén PT en planta</div></div>
      <div class="Hotspot" data-x="0.180" data-y="0.040" data-z="0.270"><div class="HotspotAnnotation">Almacén central</div></div>
      <div class="Hotspot" data-x="0.001" data-y="0.073" data-z="0.045"><div class="HotspotAnnotation">Almacén Seco y Refrigerado</div></div>
      <div class="Hotspot" data-x="-0.014" data-y="0.041" data-z="-0.230"><div class="HotspotAnnotation">CIP 2</div></div>
      <div class="Hotspot" data-x="0.098" data-y="0.046" data-z="-0.185"><div class="HotspotAnnotation">Laboratorios</div></div>
      <div class="Hotspot" data-x="-0.285" data-y="0.112" data-z="0.135"><div class="HotspotAnnotation">Bodega de Almacenamiento</div></div>
      <div class="Hotspot" data-x="-0.295" data-y="0.086" data-z="-0.095"><div class="HotspotAnnotation">Almacén PT</div></div>
      <div class="Hotspot" data-x="0.004" data-y="0.056" data-z="0.305"><div class="HotspotAnnotation">Planta de Aguas Residuales</div></div>
      <div class="Hotspot" data-x="0.042" data-y="0.073" data-z="-0.042"><div class="HotspotAnnotation">Línea San Martín</div></div>
      <div class="Hotspot" data-x="0.118" data-y="0.073" data-z="-0.050"><div class="HotspotAnnotation">Línea Krones</div></div>
      <div class="Hotspot" data-x="0.004" data-y="0.073" data-z="-0.055"><div class="HotspotAnnotation">Línea Simonazzi</div></div>
      <div class="Hotspot" data-x="0.075" data-y="0.073" data-z="-0.070"><div class="HotspotAnnotation">Línea Caraballo</div></div>
    </div>
  </div>

  <script type="module">
    import * as THREE from "three";
    import { OrbitControls } from "three/addons/controls/OrbitControls.js";
    import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";

    // Configuración básica del visor 3D
    const container = document.getElementById('visor');
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0xeef1f5);

    const camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
    camera.position.set(0, 1.5, 2.5);

    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(container.clientWidth, container.clientHeight);
    renderer.setPixelRatio(window.devicePixelRatio);
    container.appendChild(renderer.domElement);

    const controls = new OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;

    // Luz ambiental y direccional para iluminar el modelo
    const ambientLight = new THREE.AmbientLight(0xffffff, 1.2);
    scene.add(ambientLight);

    const dirLight = new THREE.DirectionalLight(0xffffff, 1.5);
    dirLight.position.set(5, 10, 7);
    scene.add(dirLight);

    // Cargar modelo GLB incorporado
    const glbData = "data:model/gltf-binary;base64,Z2xURgIAAAC06zMBwAQAAEpTT057ImJ1ZmZlclZpZXdzIjpbeyJidWZmZXIiOjAsImJ5dGVPZmZzZXQiOjAsImJ5dGVMZW5ndGgiOjg2NDc5OTIsInRhcmdldCI6MzQ5NjIsImJ5dGVTdHJpZGUiOjEyfSx7ImJ1ZmZlciI6MCwiYnl0ZU9mZnNldCI6ODY0Nzk5MiwiYnl0ZUxlbmd0aCI6Mjg4MjY2NCwidGFyZ2V0IjozNDk2M30seyJidWZmZXIiOjAsImJ5dGVPZmZzZXQiOjExNTMwNjU2LCJieXRlTGVuZ3RoIjo4NjQ3OTkyLCJ0YXJnZXQiOjM0OTYyLCJieXRlU3RyaWRlIjoxMn1dLCJhY2Nlc3NvcnMiOlt7ImJ1ZmZlclZpZXciOjAsImNvbXBvbmVudFR5cGUiOjUxMjYsImNvdW50Ijo3MjA2NjYsIm1heCI6WzAuNDAxLDAuNDg2LDAuMTEzXSwibWluIjpbLTAuNDAxMDE2MDEsLTAuNDA3NzAyLC0wLjAwNjY1ODAwMDAwMDAwMDAwMV0sInR5cGUiOiJWRUMzIn0seyJidWZmZXIiOjEsImNvbXBvbmVudFR5cGUiOjUxMjUsImNvdW50Ijo3MjA2NjYsIm1heCI6WzcyMDY2NV0sIm1pbiI6WzBdLCJ0eXBlIjoiU0NBTEFSIn0seyJidWZmZXIiOjIsImNvbXBvbmVudFR5cGUiOjUxMjYsImNvdW50Ijo3MjA2NjYsIm1heCI6WzEsMC45ODAzOTIxNTY4NjI3NDUxLDAuOTgwMzkyMTU2ODYyNzQ1MV0sIm1pbiI6WzAsMC4wNDMxMzcyNTQ5MDE5NjA3ODQsMC4wODYyNzQ1MDk4MDM5MjE1N10sInR5cGUiOiJWRUMzIn1dLCJhc3NldCI6eyJ2ZXJzaW9uIjoiMi4wIiwiZ2VuZXJhdG9yIjoiQXV0b2Rlc2suVGlua2VyY2FkIn0sIm1hdGVyaWFscyI6W3sicGJyTWV0YWxsaWNSb3VnaG5lc3MiOnsibWV0YWxsaWNGYWN0b3IiOjAuNSwicm91Z2huZXNzRmFjdG9yIjowLjV9LCJuYW1lIjoibGFtYmVydDIwU0cuMDAxIn1dLCJtZXNoZXMiOlt7InByaW1pdGl2ZXMiOlt7Im1vZGUiOjQsImF0dHJpYnV0ZXMiOnsiUE9TSVRJT04iOjAsIkNPTExPUl8wIjoyfSwiaW5kaWNlcyI6MSwibWF0ZXJpYWwiOjB9XX1dLCJzY2VuZXMiOlt7Im5vZGVzIjpbMV0sIm5hbWUiOiJUaW5rZXJjYWQgR0xURiBTY2VuZSJ9XSwic2NlbmUiOjAsIm5vZGVzIjpbeyJuYW1lIjoiTWVzaF9NZXNoX2hlYzdfZ2VvLjAwMV9sYW1iZXJ0MlNHLjAwMSIsIm1lc2giOjB9LHsibWF0cml4IjpbMSwwLDAsMCwwLDIuMjIwNDQ2MDQ5MjUwMzEzZS0xNSwtMSwwLDAsMSwyLjIyMDQ0NjA0OTI1MDMxM2UtMTYsMCwwLDAsMCwxXSwiY2hpbGRyZW4iOlswXX1dLCJidWZmZXJzIjpbeyJieXRlTGVuZ3RoIjoyMDE3ODY0OH1dfSA=";

    const loader = new GLTFLoader();
    const binaryString = atob(glbData.split(',')[1]);
    const len = binaryString.length;
    const bytes = new Uint8Array(len);
    for (let i = 0; i < len; i++) {
      bytes[i] = binaryString.charCodeAt(i);
    }

    loader.parse(bytes.buffer, '', (gltf) => {
      scene.add(gltf.scene);
      document.getElementById('cargando').style.display = 'none';
    }, (error) => {
      console.error(error);
      document.getElementById('cargando').textContent = 'Error al cargar el modelo 3D.';
    });

    // Posicionamiento dinámico de los hotspots basados en las coordenadas 3D
    const hotspots = document.querySelectorAll('.Hotspot');
    const vector = new THREE.Vector3();

    function actualizarHotspots() {
      hotspots.forEach(hotspot => {
        const x = parseFloat(hotspot.dataset.x);
        const y = parseFloat(hotspot.dataset.y);
        const z = parseFloat(hotspot.dataset.z);
        
        vector.set(x, y, z);
        vector.project(camera);

        const xCoord = (vector.x *  .5 + .5) * container.clientWidth;
        const yCoord = (vector.y * -.5 + .5) * container.clientHeight;

        if (vector.z < 1) {
          hotspot.style.display = 'block';
          hotspot.style.left = `${xCoord}px`;
          hotspot.style.top = `${yCoord}px`;
        } else {
          hotspot.style.display = 'none';
        }
      });
    }

    controls.addEventListener('change', actualizarHotspots);
    window.addEventListener('resize', () => {
      camera.aspect = container.clientWidth / container.clientHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(container.clientWidth, container.clientHeight);
      actualizarHotspots();
    });

    function animate() {
      requestAnimationFrame(animate);
      controls.update();
      renderer.render(scene, camera);
      actualizarHotspots();
    }
    animate();
  </script>
</body>
</html>
