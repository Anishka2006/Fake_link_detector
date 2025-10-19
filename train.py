def is_fake_link(url):
    url = url.lower()
    fake_indicators = [
        "fake",
        "scam",
        "phishing",
        "fraud",
        "malware",
        "spam",
        "login",
        "verify",
        "update",
        "secure",
        "account",
        "banking",
        "password",
        "click here",
        "urgent",
        "limited time",
        "winner",
        "congratulations",
        "free",
        "confirm"]
    
    #check if http or https is missing
    if not url.startswith("http://") or url.startswith("https://"):
        return True, "No HTTP/HTTPS found"
    
    #check if @ is missing
    if "@" in url:
        return True, "Contains @ symbol"
    
    #count too many dots or hyphens
    if url.count(".") > 5 or url.count("-") > 4:
        return True, "Too many dots or hyphens"
    
    #check for suspicious keywords
    for indicator in faske_indicators:
        if(indicator in url):
            return True, "Contains suspicious keyword:" + indicator

    #check if url is too long
    if(len(url) > 75):
        return True, "Too long url"

    #if no issues found
    return False, "Safe url"