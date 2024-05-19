# # This is a sample Python script.
#
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharmm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

print("xin chào, đây là dòng đầu tiên")
bang_chu_cai = ["a","b","c","d","e","f","g","h","i","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
##print(bang_chu_cai);

Secret = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

result = ""

for i in Secret:
    if i == " " or i == "." or i == "(" or i == ")" or i == "'":
        result += i
        continue
    else:
        for i1 in bang_chu_cai:
            if i == i1:
                index_change = bang_chu_cai.index(i1) + 2;
                if index_change >= 25:
                    index_change = index_change - 25
                result = result + bang_chu_cai[index_change]


print(result)

