# String operations

languages = ["Java","Python","Ruby","Rust","Elexer", "Js","Cpp","C"]

def startwith_listcomprihension(languages,startwith):
    reqlist = [language for language in languages if language[0]==startwith]
    return reqlist


def startwith_logic_function(languages,startwith):
    required_list = []
    for language in languages:
        if language[0]==startwith:
            required_list.append(language)
    return required_list

def startwith_pre_define_func(languages, startwith):
    required_list = []
    for language in languages:
        if language.startswith(startwith):
            required_list.append(language)
    return required_list


print(startwith_listcomprihension(languages,"J"))
print(startwith_logic_function(languages,"R"))
print(startwith_pre_define_func(languages,"C"))

def adv_fun():
    