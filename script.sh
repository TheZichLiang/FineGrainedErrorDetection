srun --qos=default --account=class --partition=class --gres=gpu:1 --mem=32g --time=01:00:00 bash -c "python test.py &> test.out"
