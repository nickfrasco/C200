# parameter: areacode the area code of the phone number
# return: state or "unknown"
def area_lookup(areacode):
    if areacode == 205 or 251 or 256 or 334 or 938:
        print("Alabama")
    elif areacode == 907:
        print("Alaska")
    elif areacode == 684:
        print("American Samoa")
    elif areacode == 480 or 520 or 602 or 623 or 928 :
        print("Arizona")
    elif areacode == 479 or 501 or 870:
        print("Arkansas")
    elif areacode == 209 or 213 or 310 or 323 or 408 or 415 or 424 or 442 or 510 or 530 or 559 or 562 or 619 or 626 or 628 or 650 or 657 or 661 or 669 or 707 or 714 or 747 or 760 or 805 or 818 or 831 or 858 or 909 or 916 or 925 or 949 or 951: 
        print("California")
    elif areacode == 303 or 719 or 720 or 970:
        print("Colorado")
    elif areacode == 203 or 475 or 860 or 959: 
        print("Connecticut")
    elif areacode == 302: 
        print("Delaware ")
    elif areacode == 239 or 305 or 321 or 352 or 386 or 407 or 561 or 727 or 754 or 772 or 786 or 813 or 850 or 863 or 904 or 941 or 954: 
        print("Florida")
    elif areacode == 229 or 404 or 470 or 478 or 678 or 706 or 762 or 770 or 912: 
        print("Georgia")
    elif areacode == 671: 
        print("Guam")
    elif areacode == 808: 
        print("Hawaii")
    elif areacode == 208: 
        print("Idaho")
    elif areacode == 217 or 224 or 309 or 312 or 331 or 618 or 630 or 708 or 773 or 779 or 815 or 847 or 872: 
        print("Illinois")
    elif areacode == 219 or 260 or 317 or 463 or 574 or 765 or 812 or 930: 
        print("Indiana")
    elif areacode == 319 or 515 or 563 or 641 or 712: 
        print("Iowa")
    elif areacode == 316 or 620 or 785 or 913: 
        print("Kansas")
    elif areacode == 270 or 364 or 502 or 606 or 859: 
        print("Kentucky")
    elif areacode == 225 or 318 or 337 or 504 or 985: 
        print("Louisiana")
    elif areacode == 207: 
        print("Maine")
    elif areacode == 240 or 301 or 410 or 443 or 667: 
        print("Maryland")
    elif areacode == 339 or 351 or 413 or 508 or 617 or 774 or 781 or 857 or 978: 
        print("Massachusetts")
    elif areacode == 231 or 248 or 269 or 313 or 517 or 586 or 616 or 734 or 810 or 906 or 947 or 989: 
        print("Michigan")
    elif areacode == 218 or 320 or 507 or 612 or 651 or 763 or 952: 
        print("Minnesota")
    elif areacode == 228 or 601 or 662 or 769: 
        print("Mississippi")
    elif areacode == 314 or 417 or 573 or 636 or 660 or 816: 
        print("Missouri")
    elif areacode == 406: 
        print("Montana")
    elif areacode == 308 or 402 or 531: 
        print("Nebraska")
    elif areacode == 702 or 725 or 775: 
        print("Nevada")
    elif areacode == 603: 
        print("New Hampshire")
    elif areacode == 201 or 551 or 609 or 732 or 848 or 856 or 862 or 908 or 973: 
        print("New Jersey")
    elif areacode == 505 or 575: 
        print("New Mexico")
    elif areacode == 212 or 315 or 332 or 347 or 516 or 518 or 585 or 607 or 631 or 646 or 680 or 716 or 718 or 845 or 914 or 917 or 929 or 934: 
        print("New York")
    elif areacode == 252 or 336 or 704 or 743 or 828 or 910 or 919 or 980 or 984: 
        print("North Carolina")
    elif areacode == 701: 
        print("North Dakota") 
    elif areacode == 670: 
        print("Northern Mariana Islands")
    elif areacode == 216 or 220 or 234 or 330 or 380 or 419 or 440 or 513 or 567 or 614 or 740 or 937: 
        print("Ohio")
    elif areacode == 405 or 539 or 580 or 918: 
        print("Oklahoma")
    elif areacode == 458 or 503 or 541 or 971: 
        print("Oregon")
    elif areacode == 215 or 267 or 272 or 412 or 484 or 570 or 610 or 717 or 724 or 814 or 878: 
        print("Pennsylvania")
    elif areacode == 787 or 939: 
        print("Puerto Rico")
    elif areacode == 401: 
        print("Rhode Island")
    elif areacode == 803 or 843 or 854 or 864: 
        print("South Carolina")
    elif areacode == 605: 
        print("South Dakota")
    elif areacode == 423 or 615 or 629 or 731 or 865 or 901 or 931: 
        print("Tennessee")
    elif areacode == 210 or 214 or 254 or 281 or 325 or 346 or 361 or 409 or 430 or 432 or 469 or 512 or 682 or 713 or 737 or 806 or 817 or 830 or 832 or 903 or 915 or 936 or 940 or 956 or 972 or 979: 
        print("Texas")
    elif areacode == 385 or 435 or 801: 
        print("Utah")
    elif areacode == 802: 
        print("Vermont")
    elif areacode == 340: 
        print("Virgin Islands")
    elif areacode == 276 or 434 or 540 or 571 or 703 or 757 or 804: 
        print("Virginia")
    elif areacode == 206 or 253 or 360 or 425 or 509: 
        print("Washington")
    elif areacode == 202: 
        print("Washington DC")
    elif areacode == 304 or 681: 
        print("West Virginia")
    elif areacode == 262 or 414 or 534 or 608 or 715 or 920: 
        print("Wisconsin")
    elif areacode == 307: 
        print("Wyoming")
    else:
        print("Unknown") 


# parameter: pn is the phone number
# return: True , False if grammatically correct
def parse_phone(pn):
    for i in pn:
        for x in [chr(i) for i in range(ord('A'),ord('Z'))]:
            if i == x:
                return False
            else:
                return True



# parameter: pn is a string that is a possible phone number
# return: "bad syntax" if the number isn’t correctly formed,
#the state if the area code is described in the file, or
#"unknown" if formed correctly, but not in state file
def phone_number(pn):
    if pn[0] == "(" and pn[4] == ")" and pn[5] == "-" and pn[9] == "-":
        print(area_lookup(pn))
    else:
        print("bad syntax")


pnlst = ["(440)-342-2223", "(453)-314-1111","(123)-666-4142","(241)-142-11A3"]

for i in pnlst:
    print(phone_number(i))
