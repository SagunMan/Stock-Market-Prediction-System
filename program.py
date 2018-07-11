from train import getProbsAndPreds
from train import train

def main(val):
    from input import get_traindata
    train_data = get_traindata(val)
    train(train_data)
    
def get_prediction(val):
    from input import get_testdata,get_value
    
        
    test_data = get_testdata(val)
    preds = getProbsAndPreds(test_data)
    
    values = get_value(val)
    diff = float(values[2])+(preds[0])
    maxprice = float(values[3])+(preds[1])
    minprice = float(values[4])+(preds[2])
    amount = float(values[5])+preds[3]
    shares = float(values[6])+preds[4]
    trans = float(values[7])+preds[5]

    output = []
    output.append('comany alias: ' + values[0])
    output.append('company name: ' + values[1])
    output.append('closing price prediction: ' + str(int(diff)))
    output.append('max price prediction: ' + str(int(maxprice)))
    output.append('min price prediction: ' + str(int(minprice)))
    output.append('amount prediction: ' + str(int(amount)))
    output.append('Traded shares prediction: ' + str(int(shares)))
    output.append('No of transactions prediction: ' + str(int(trans)))
    
    print('accuracy:' + str(get_accuracy(val)))
    
    return output
    

def get_outcome(val):
    from input import get_testdata
    
    test_data = get_testdata(val)
    preds = getProbsAndPreds(test_data)
        
    output = []
    output.append(preds[0])
    output.append(preds[1])
    output.append(preds[2])

    return output

def get_accuracy(val):
    from input import get_testdata,get_value,get_accdata
        
    diffa = 0
    maxa = 0
    mina = 0
    amounta = 0
    sharesa = 0
    transa = 0
    
    test_data = get_testdata(val)
    preds = getProbsAndPreds(test_data)
    acc = get_accdata(val)
    
    values = get_value(val)
    diff = float(values[2])+(preds[0])
    maxprice = float(values[3])+(preds[1])
    minprice = float(values[4])+(preds[2])
    amount = float(values[5])+preds[3]
    shares = float(values[6])+preds[4]
    trans = float(values[7])+preds[5]
    
    if(diff<acc[0]):
        diffa = (diff/acc[0])*100
    if(diff>acc[0]):
        diffa = (acc[0]/diff)*100
    if(maxprice<acc[1]):
        maxa = (maxprice/acc[1])*100
    if(maxprice>acc[1]):
        maxa = (acc[1]/maxprice)*100
    if(minprice<acc[2]):
        mina = (minprice/acc[2])*100
    if(minprice>acc[2]):
        mina = (acc[2]/minprice)*100
    if(amount<acc[3]):
        amounta = (amount/acc[3])*100
    if(amount>acc[3]):
        amounta = (acc[3]/amount)*100
    if(shares<acc[4]):
        sharesa = (shares/acc[4])*100
    if(shares>acc[4]):
        sharesa = (acc[4]/shares)*100
    if(trans<acc[5]):
        transa = (trans/acc[4])*100
    if(trans>acc[5]):
        transa = (acc[5]/trans)*100
        
    accuracy = (diffa+maxa+mina+amounta+sharesa+transa)/6
    
    return accuracy