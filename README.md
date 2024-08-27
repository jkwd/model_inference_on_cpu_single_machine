# model_inference_on_cpu_single_machine

# Init
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# Experiments
Tested on: 
1. vanilla python
2. spark
3. ray
4. celery

To run 1-3, you can simply run the following commands:
```
cd src
python3 baseline_main.py
python3 spark_main.py
python3 ray_main.py
```

To run celery, it requires more effort. It requires redis and celery to be started 1st:
1. In terminal 1, run `docker run --name redis -p 6379:6379 -d redis`. This will run redis in detached mode.
2. In termial 1, activate `.venv` and run `celery -A tasks worker --loglevel=INFO --concurrency=2`. This will start up celery.
3. In terminal 2
   1. Activate `.venv` and run `python3 celery_main.py`

# Results
Baseline: 696.1332404613495
Ray: 601.8566570281982

If task is simple then Ray will be an overhead