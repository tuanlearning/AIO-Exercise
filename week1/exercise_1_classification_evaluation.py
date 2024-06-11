# Exercise 1: write a function with 3 inputs: tp, fp, fn and produce outputs: precision, recall, f1-score
# tp,fp and fn must be integer and > 0
def compute_metrics(tp,fp,fn):
    assert isinstance(tp,int), "tp should be int"
    assert isinstance(fp,int), "fp should be int"
    assert isinstance(fn,int), "fn should be int"
    assert tp > 0 and fp > 0 and fn > 0, "tp and fp and fn must be greater than zero"
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1_score = 2*(precision*recall)/(precision+recall)
    print(f'precision is {precision}')
    print(f'recall is {recall}')
    print(f'f1_score is {f1_score}')

compute_metrics(2,3,4)