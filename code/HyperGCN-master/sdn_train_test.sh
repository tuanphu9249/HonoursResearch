#!/bin/sh


echo "depth 2, 1k" >> sdn_eval_result.txt
python3 hypergcn.py --data sdn --dataset sdn_1k_1  --rate 0.02 --depth 2 --decay 0.0001 --split 1 --epochs 200 >> sdn_eval_result.txt


echo "depth 4, 1k" >> sdn_eval_result.txt
python3 hypergcn.py --data sdn --dataset sdn_1k_1  --rate 0.02 --depth 4 --decay 0.0001 --split 1 --epochs 200 >> sdn_eval_result.txt


echo "depth 5, 1k" >> sdn_eval_result.txt
python3 hypergcn.py --data sdn --dataset sdn_1k_1  --rate 0.02 --depth 5 --decay 0.0001 --split 1 --epochs 200 >> sdn_eval_result.txt

echo "depth 2, 4k" >> sdn_eval_result.txt 
python3 hypergcn.py --data sdn --dataset sdn_4k_1  --rate 0.02 --depth 2 --decay 0.0001 --split 1 --epochs 200 >> sdn_eval_result.txt

echo "depth 3, 4k" >> sdn_eval_result.txt
python3 hypergcn.py --data sdn --dataset sdn_4k_1  --rate 0.02 --depth 3 --decay 0.0001 --split 1 --epochs 200 >> sdn_eval_result.txt


echo "depth 4, 4k" >> sdn_eval_result.txt
python3 hypergcn.py --data sdn --dataset sdn_4k_1  --rate 0.02 --depth 4 --decay 0.0001 --split 1 --epochs 200 >> sdn_eval_result.txt


