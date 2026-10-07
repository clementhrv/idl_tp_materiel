# Ma machine

| Question | Réponse |
|---|---|
| Processeur, architecture | Intel Core i5-1135G7, x86-64 |
| Sockets / cœurs / threads | 1 / 4 / 8|
| Cœurs P / E | 4/0 |
| Fréquence de base / max | 2.40GHz / 4.20GHz |
| L1d / L2 / L3, ligne | 192 KiB / 5 MiB / 8 MiB, 64|
| Caches partagés? | L1 et L2 privés par cœur, L3 partagé entre les 4 cœurs |
| SIMD et largeur | SSE4.1/SSE4.2 (128 bits), AVX/AVX2 (256 bits), AVX-512 (512 bits) |
| Mémoire: capacité, type, canaux | 3,8 Go de RAM visibles par WSL, 1,46 GiB de RAM; type et nombre de canaux non accessibles depuis WSL2 |
| FMA | yes |

## Crête

- Double précision: 448.0 Gflop/s
- Simple précision: 896.0 Gflop/s
- Bande passante mémoire théorique: 51.2 Go/s
- Intensité arithmétique d'équilibre: 8.75 flop/octet

## Énergie (optionnel)

- Au repos: … W
- Un cœur occupé: … W
