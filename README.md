# model_inference_on_cpu_single_machine

# Experiments
Tested on: 
1. vanilla python
2. spark
3. ray
4. celery

# Running the experiment
1. Download [docker](https://docs.docker.com/get-started/get-docker/)
2. 

# Results
## Baseline
Translation: 6571.11203122139 6580.369368553162
Sentiment: 130.70904088020325 138.09011006355286

## Ray
Translation: 2435.978399991989 2448.489275455475
Sentiment: 193.55180501937866 204.73267912864685


If task is simple then Ray will be an overhead