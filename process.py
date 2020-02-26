def scoring(i_name,i_mno,i_ug,i_ugy,i_pg,i_pgy,r_py,r_r,r_ds,c_ml,c_dl,c_nlp,c_sts,c_aws,c_sql,c_excel):
    score = 0
    # UG score
    try:   
        if int(i_ugy) == 2020:
            score = score+10
    except:
        ""
    try:
        if int(i_ugy) == 2019:
            score = score+8
    except:
        ""
    try:
        if int(i_ugy) <= 2018:
            score = score+5
    except:
        ""
    # Pg Score
    try:
        if int(i_pgy) == 2020:
            score = score+7
    except:
        ""
    try:
        if int(i_pgy) <= 2019:
            score = score+3
    except:
        ""
    # Python rating score
    if r_py == "3":
        score = score+10
    if r_py == "2":
        score = score+7
    if r_py == "1":
        score = score+3
    # R Programming
    if r_r == "3":
        score = score+10
    if r_r == "2":
        score = score+7
    if r_r == "1":
        score = score+3
    # Dtaa Science
    if r_ds == "3":
        score = score+10
    if r_ds == "2":
        score = score+7
    if r_ds == "1":
        score = score+3
    # Achine learning score
    checkbox = [c_ml,c_dl,c_nlp,c_sts,c_aws,c_sql,c_excel].count('on')
    score = score + (checkbox*3)
    return score
    
    
     
    