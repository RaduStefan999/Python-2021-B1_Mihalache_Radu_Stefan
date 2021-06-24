def aply_rule(rule, string) :
    return (string.startswith(rule[1]) and string.find(rule[2]) and string.endswith(rule[3]))

def validate_rules (rules, strings) :

    rules_status = True

    for key in strings :
        
        OK = False

        for tuplu in rules :
            if (tuplu[0] == key) :
                OK = True
                rules_status = rules_status and aply_rule(tuplu, d[key])

        if OK == False : return False

    return rules_status


s = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
d = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}

print (validate_rules(s, d))