# Ma montagne mémoire

Machine : Intel Core i5-1135G7, x86-64, sous WSL2.

| Niveau | Taille déduite | Taille TP1 | Débit |
|---|---:|---:|---:|
| L1 | 32–64 Kio | 48 Kio | ~40 Go/s |
| L2 | 1–2 Mio | 1,25 Mio | ~35 Go/s |
| L3 | 4–8 Mio | 8 Mio | ~25 Go/s |
| RAM | > 8 Mio | 3,8 Go disponibles | ~17 Go/s |

Taille de ligne : **64 octets** (confirmée par `getconf`).

## Réponses

1. Le débit baisse vers 64 Kio, 2 Mio et 8 Mio : ce sont les passages respectifs du L1, du L2 et du L3.

2. Les débits sont environ 32 Go/s en L1, 30 Go/s en L2, 17 Go/s en L3  (correspondance des creux sur mountain_stride1.png) et 17 Go/s en RAM. Le L1 est donc environ 2 fois plus rapide que la RAM.

3. Pour un tableau de 64 Mio, le débit baisse quand le pas augmente, car une ligne de cache est chargée mais peu utilisée. Le débit se stabilise vers le pas 8 : `8 × 8 octets = 64 octets`. La ligne de cache fait donc 64 octets. C'est également la valeur obtenue en faisant la commande donnée.

4. Pour un tableau qui tient dans le L1, le pas a peu d'effet comme on le voit sur la figure mountain_stride32K.png: les données sont déjà dans le cache le plus rapide.

