def lambda_handler(event, context):
    import csv
    import urllib2
    import random
    
    T = int(event['T'])
    com = str(event['com'])
    investment = float(event['investment'])
    M = int(event['M'])
    
    #PARAMETERS
    #com = 'amazon'
    #T = 100
    #investment = 1000
    #M

    url = 'https://s3.eu-west-2.amazonaws.com/hud123/' + com + '.csv'
    response = urllib2.urlopen(url)
    cr = csv.reader(response, delimiter=',', quotechar='"')
    
    dsets = []
    for row in cr:
        dsets.append(row[6])
        #dsets = str(dsets) 
    
    ########################
    adj = dsets
    ########################
    #ADJACENT CLOSE
    if T <= len(adj) - 1:
        pass
    else:
        T = len(adj) - 1
        #print ' '
        #print 'Please enter  ::VALID_DATAPOINT::'
        #print 'since, T is INVALID, we assign the maximun length of DATAPOINTs, as shown below :\n'
        #print T
        #print ' '
    adj = adj[1:T]
    int_l = [ ]
    for num in adj:
        adj_c = float(num)
        int_l.append(adj_c)
    int_l = int_l[:]    
    
    ########################
    s = int_l 
    ########################
    #RETURN SERIES
    days = len(s) - 1
    t_rets = [ ]
    for n in range(0,days):
        ret = (s[n]-s[n+1])/s[n+1]
        t_rets.append(ret)
        
    ########################
    c = t_rets
    ########################
    #SORT
    c = c#.values.tolist()
    c = list(c)
    c.sort(reverse = True)
    
    ########################
    r_s = c
    ########################
    #HISTORICAL
    ret_len = len(r_s) - 1
    loss_value_at_95 = (95 * ret_len) / 100
    r_s95 = r_s[int(loss_value_at_95)]
    loss_value_at_99 = (99 * ret_len) / 100
    r_s99 = r_s[int(loss_value_at_99)]
    investment = int(investment)
    his_var_95 = investment * r_s95
    his_var_99 = investment * r_s99
    ########################
    l = t_rets
    ########################
    #MEAN
    mean = float(sum(l)) / max(len(l), 1)
    vrs = t_rets
    ########################
    #STD
    ss = sum((x-mean)**2 for x in vrs)
    n = len(t_rets)
    pvar = ss/n
    std = pvar**0.5
    ########################
    adjc = int_l
    #M
    #investment
    #mean,
    #std,
    ########################
    
    ########################
    #COVARIANCE
    investment = int(investment)
    #VAR at 95% is found at 1.65 std from the mean
    cor_var95 = -(mean + (1.65 * std)) * investment
    #VAR at 99% is found at 2.33 std from the mean
    cor_var99 = -(mean + (2.33 * std)) * investment
    ########################
    
    #MONTE CARLO
    new_prices = [ ]
    randm = [ ]
    p = adjc[0]
    for m in range(0,M):
        q = random.gauss(mean,std)
        randm.append(q)
    for u in range(0,M):
        n = (1 + randm[u]) * p
        new_prices.append(n)
        #return new_prices
    
    ######################## 
    m_c = new_prices
    ########################    
    #SORT
    m_c = m_c#.values.tolist()
    m_c = list(m_c)
    m_c.sort(reverse = True)
    ########################
    m_r_s = m_c
    ########################
    #MONTE_HISTORIAL
    m_ret_len = len(m_r_s) - 1
    m_loss_value_at_95 = (95 * m_ret_len) / 100
    m_r_s95 = m_r_s[int(m_loss_value_at_95)]
    m_loss_value_at_99 = (99 * m_ret_len) / 100
    m_r_s99 = m_r_s[int(m_loss_value_at_99)]
    investment = int(investment)
    mont_var_95 = investment * m_r_s95
    mont_var_99 = investment * m_r_s99
    
    
    return his_var_95, his_var_99, cor_var95, cor_var99,mont_var_95, mont_var_99
