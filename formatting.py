def fail_ok(value, center):
    '''
    Terminal coloring text with red and green and centering the content.
    '''
    if value.startswith("-"):
        #return f"{bcolors.FAIL}{value:^{center}}{bcolors.ENDC}"
        return f"\033[91m{value:^{center}}\033[0m"
    elif value.startswith("+"):
        return f"\033[92m{value:^{center}}\033[0m"
    else:
        return f"{value:^{center}}"
