
```mermaid
graph TD
    AA[Método PERT] -->|Contexto aleatorio| AB
    AA -->|Calendario de ejecución del proyecto| AC
    AA -->|Conceptos de holgura y camino crítico| AD
    AA -->|Cálculo de los tiempos EET y LET| AE
    AA -->|Asignación de tiempos a las actividades| AF
    AA -->|Construcción del grafo PERT| AG
    AA -->|Principios básicos| AH
    AB -->|Función de densidad de probabilidad Beta| AI["f(t) = K(t-a)^(α)(b-t)^(β)"]
    AB -->|Asimetría de la distribución| AJ["Asimetría: (a+b)/2 ≠ m"]
    AC -->|Fechas de comienzo y finalización| AK["Hij' = Δij' - Vij'"]
    AD -->|Holgura y camino crítico| AL["Hi = ti*' - ti, Hij' = ti*' - ti - tij"]
    AE -->|EET y LET| AM["EET: tj = max[ti + tij], LET: ti* = min[ti*' - tij]"]
    AF -->|Estimaciones de tiempo| AN["D = (Eo + 4Em + Ep)/6, Varianza: v^2 = ((Eo-Ep)/6)^2"]
    AG -->|Sucesos de inicio y fin| AO["Inicio: ti = 0, Fin: ti* = max[ti + tij]"]
    AH -->|Prelaciones entre actividades| AP["Lineales, Convergencia, Divergencia"]

    

  
```



















```mermaid
graph TD
    A[Método ROY] -->|Holguras y calendario de ejecución| B
    A -->|Cálculo de tiempos mínimo y máximo| C["Tk = max #40;Tj + Dj#41;, Tk* = min #40;TL* - Dk#41;"]
    B -->|Holgura total Hk^T| E["Hk^T = Tk* - Tk"]
    B -->|Holgura libre Hk^L| F["Hk^L = min #40;Tl - Tk - Dk#41;"]
    B -->|Calendario de ejecución| G["Δk = Tk, Vk = Tk + Dk"]

```






