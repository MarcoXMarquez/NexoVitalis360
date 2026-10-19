# 05 - Vista Física (Hito 2 / NexoVitalis360)

## 1. Directriz y Regla Estricta de Cátedra (M.Sc. Percy Oscar Huertas Niquén)
> *"¿Qué contiene la vista física? El software y el hardware. Tienen que hacer un diagrama en el cual se note cómo usted va a utilizar el software y el hardware dentro de la construcción del sistema. ¿Dónde está eso? En los **requisitos no funcionales**.
> Coloquen los gráficos que tengan la mejor **affordance** para representar la arquitectura: un celular, una tablet, una laptop, un computador, el servidor rack tal como debe ser.
> En la parte de software tienen que colocar qué lenguaje de programación, qué librerías van a utilizar, qué componentes van a utilizar, incluidos los protocolos de comunicación y puertos.
> **Todo lo que está aquí tiene que aparecer en los requisitos no funcionales**. El hardware tiene que reflejar con qué máquinas cuenta su cliente, el sistema operativo, su versión y la memoria virtual (`pagefile.sys`)."*

---

## 2. Artefactos y Diagrama de Despliegue Oficial

### Figura 7.1: Diagrama de Despliegue UML 2.5 e Infraestructura Hardware/Software
- **Archivo Interactivo HTML:** [`Figura_5_1_Vista_Fisica_Despliegue_v01.00.html`](file:///C:/Users/marco/Desktop/TEO-DAS/DAS-GITHUB/05_DIAGRAMAS_Y_RECURSOS_EDITABLES/05_Vista_Fisica/Figura_5_1_Vista_Fisica_Despliegue_v01.00.html) / [`fig5_1_vista_fisica_despliegue.html`](file:///C:/Users/marco/Desktop/TEO-DAS/DAS-GITHUB/05_DIAGRAMAS_Y_RECURSOS_EDITABLES/05_Vista_Fisica/fig5_1_vista_fisica_despliegue.html)
- **Render Gráfico Oficial (300 DPI):** [`Figura_5_1_Vista_Fisica_Despliegue_v01.00.png`](file:///C:/Users/marco/Desktop/TEO-DAS/DAS-GITHUB/05_DIAGRAMAS_Y_RECURSOS_EDITABLES/05_Vista_Fisica/Figura_5_1_Vista_Fisica_Despliegue_v01.00.png)
- **Script Generador Python:** `scripts/12_diagrama_vista_fisica_despliegue.py`

---

## 3. Topología de Red en 4 Zonas Físicas y Cobertura RNF

### Zona 1: Estaciones Cliente y Dispositivos Móviles (Multi-Fabricante)
- **Workstation Consultorio Médico (`«device: workstation»`):** Intel Core i5-12400 (6 Cores 4.4 GHz), 16GB RAM DDR4, SSD 512GB NVMe, Monitor IPS 24" Full HD. Software: Windows 11 Pro 64-bit con archivo de paginación obligatorio `pagefile.sys 8GB`, Google Chrome v124+ / Microsoft Edge, SPA React 18 con WebSockets. (*RNF-0001, RNF-0003, RNF-0010*).
- **Laptop Recepción y Caja (`«device: laptop»`):** Laptop HP ProBook 450 G9 (Intel Core i5-1235U, 16GB RAM, SSD 256GB), Impresora Térmica EPSON TM-T20III USB/Ethernet. Software: Windows 11 Pro, `pagefile.sys 8GB`, driver EPSON ESC/POS. (*RNF-0001, RNF-0015*).
- **Smartphones Tutor/Paciente (`«device: mobile»`):** Dispositivos móviles multi-fabricante (Samsung OneUI Android 12-14, Xiaomi MIUI, Motorola, Apple iOS 17+), conectividad 4G/5G y WiFi. Aplicación: PWA Offline-ready con Service Workers. (*RNF-0002, RNF-0018*).
- **Tablet Hospitalaria Enfermería/Triaje (`«device: tablet»`):** Samsung Galaxy Tab Active4 Pro Ruggedized (Snapdragon 778G, 6GB RAM, WiFi 6, NFC). Software: Android 14 Enterprise con Samsung Knox Security Suite. (*RNF-0002, RNF-0016*).

### Zona 2: Red Perimetral, Seguridad DMZ y Balanceo
- **Firewall Perimetral & WAF (`«appliance: security»`):** Fortinet FortiGate 60F Appliance / AWS WAF Layer 7. Software: FortiOS 7.4 con reglas OWASP CRS v3.3, mitigación de ataques DDoS y Rate Limiting (100 req/min por IP). (*RNF-0004, RNF-0006, RNF-0021*).
- **Reverse Proxy & Load Balancer (`«server: proxy»`):** NGINX Plus 1.25 sobre Alpine Linux minimalista endurecido. Terminación SSL/TLS 1.3, balanceo Least Connections y redirección forzada de TCP 80 a TCP 443 HTTPS. (*RNF-0005, RNF-0008*).

### Zona 3: Cluster de Aplicación y Microservicios (Subred Privada App)
- **Servidor Primario de Aplicaciones (`«execution-environment»`):** Servidor Rack HP ProLiant DL380 Gen10 (2x Intel Xeon Silver 4314 32 Cores, 64GB RAM ECC, 2x SAS 600GB 15K RAID 1). Host: Ubuntu Server 22.04 LTS (Swap 16GB). Contenedores Docker: Core Spring Boot 3.2.4 en JVM Eclipse Temurin OpenJDK 21 LTS y Motor Bonita BPM Community 2024.1. (*RNF-0007, RNF-0009, RNF-0011, RNF-0013*).
- **Microservicio Facturación SUNAT UBL 2.1 (`«execution-environment»`):** Contenedor Docker aislado (4 vCPU, 8GB RAM). Node.js 20 LTS, OpenSSL 3.0, XMLSec con Certificado Digital X.509 en HSM criptográfico y cliente SOAP con timeout de 15 segundos. (*RNF-0012, RNF-0017*).

### Zona 4: Persistencia, Storage y Servicios Externos Cloud
- **Servidor Primario Base de Datos PostgreSQL 16 (`«device: db-server»`):** Dell PowerEdge R750 (Intel Xeon Gold 5318Y, 64GB RAM ECC, 4x 1.92TB NVMe SSD RAID 10 con 120,000 IOPS). PostgreSQL 16.2 Enterprise 64-bit con `shared_buffers = 16GB` y Replicación Síncrona WAL Streaming hacia nodo secundario. (*RNF-0014, RNF-0019, RNF-0020, RNF-0022*).
- **Servidor de Almacenamiento MinIO / S3 Blob (`«device: storage-server»`):** NAS Storage con 16TB en RAID 6. MinIO Enterprise con cifrado en reposo SSE-KMS / AES-256 para historias clínicas, recetas y CDRs. (*RNF-0023, RNF-0024, RNF-0025*).
- **Servicios Externos Cloud (TLS 1.3 Outbound):** Google Meet API (Teleconsultas), SUNAT/OSE Web Service (Facturación), Pasarela Niubiz (PCI-DSS v4.0), Twilio/Meta WhatsApp API (Notificaciones).

---

## 4. Matriz de Correspondencia Bidireccional con RNF-0001 a RNF-0025
Todos los 25 requisitos no funcionales del Catálogo de Requisitos están explícitamente mapeados con sus badges técnicos en las tarjetas del visor interactivo y en el diagrama de despliegue gráfico.
