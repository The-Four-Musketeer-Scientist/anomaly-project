def compute_pct_b(pages, span, weight, user):
    midband = train.ewm(span=span).mean()
    stdev = train.ewm(span=span).std()
    ub = midband + stdev*weight
    lb = midband - stdev*weight
    bb = pd.concat([ub, lb], axis=1)
    df = pd.concat([pages, midband, bb], axis=1)
    df.columns = ['pages', 'midband', 'ub', 'lb']
    df['pct_b'] = (df['pages'] - df['lb'])/(df['ub'] - df['lb'])
    df['user_id'] = user
    return df

def plt_bands(my_df, user):
    fig, ax = plt.subplots(figsize=(12,8))
    ax.plot(df.index, df.pages, label='Number of Pages, User: '+str(user))
    ax.plot(df.index, df.midband, label = 'EMA/midband')
    ax.plot(df.index, df.ub, label = 'Upper Band')
    ax.plot(df.index, df.lb, label = 'Lower Band')
    ax.legend(loc='best')
    ax.set_ylabel('Number of Pages')
    plt.show()

def find_anomalies(df, user, span, weight):
    pages = prep(df, user)
    df = compute_pct_b(pages, span, weight, user)
    
    return df[df.pct_b>1]
