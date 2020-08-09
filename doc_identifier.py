import word_retriever as wr
import ImageAlignment as ia
import shutil, os
import os.path


def get_doc_type(doc):
    '''
    Method to identify docs.
    '''
    # Cheque
    loc1 = ia.find_word_location(doc, 'validfor3month')
    loc2 = ia.find_word_location(doc, 'validforthreemonth')
    loc3 = ia.find_word_location(doc, 'pay')
    loc4 = ia.find_word_location(doc, 'bank')
    loc5 = ia.find_word_location(doc, 'rupees')
    loc6 = ia.find_word_location(doc, 'bearer')
    if ((loc1 is not None or loc2 is not None) or loc3 is not None) and loc4 is not None and loc5 is not None and loc6 is not None:
        return "cheque"

    # Passbook
    loc1 = ia.find_word_location(doc, 'account')
    loc2 = ia.find_word_location(doc, 'name')
    loc3 = ia.find_word_location(doc, 'withdrawal')
    loc4 = ia.find_word_location(doc, 'deposit')
    loc5 = ia.find_word_location(doc, 'balance')
    loc6 = ia.find_word_location(doc, 'date')
    loc8 = ia.find_word_location(doc, 'bank')
    if (loc1 is not None and loc2 is not None and loc6 is not None and loc8 is not None) or (loc3 is not None and loc4 is not None and loc5 is not None):
        return "passbook"

    # Aadhaar
    loc1 = ia.find_word_location(doc, 'governmentofindia')
    loc2 = ia.find_word_location(doc, 'yearofbirth')
    loc3 = ia.find_word_location(doc, 'uniqueidentificationauthorityofindia')
    loc4 = ia.find_word_location(doc, 'address')
    loc5 = ia.find_word_location(doc, 'aadhaar')
    loc6 = ia.find_word_location(doc, 'dob')
    loc7 = ia.find_word_location(doc, 'male')
    if (loc1 is not None and (loc2 is not None or loc6 is not None or loc7 is not None)) or (loc3 is not None and loc4 is not None) or loc5 is not None:
        return "aadhaar"

    # VoterID
    set1 = ['elector', 'father', 'age', 'sex']
    set2 = ['name', 'father']
    set3 = ['address', 'thiscardcanbeused', 'governmentprogrammes']
    set4 = ['address', 'age', 'sex', 'note', 'merepossession']
    card_type = ""

    count = 0
    for word in set1:
        loc = ia.find_word_location(doc, word)
        loc1 = ia.find_word_location(doc, 'father')
        if loc is not None:
            count += 1
            if count == 3 and loc1 is not None:
                card_type = "oldCard_1"
                break

    count = 0
    for word in set2:
        loc = ia.find_word_location(doc, word)
        loc1 = ia.find_word_location(doc, 'age')
        loc2 = ia.find_word_location(doc, 'sex')
        if loc is not None and loc1 is None and loc2 is None:
            count += 1
            if count == 2:
                card_type = "newCard_1"
                break

    if card_type == "":
        count = 0
        for word in set3:
            loc = ia.find_word_location(doc, word)
            if loc is not None:
                count += 1
                if count == 3:
                    card_type = "oldCard_2"
                    break
        if card_type == "":
            count = 0
            for word in set4:
                loc = ia.find_word_location(doc, word)
                if loc is not None:
                    count += 1
                    if count == 5:
                        card_type = "newCard_2"
                        break
    if card_type == "oldCard_1" or card_type == "oldCard_2" or card_type == "newCard_1" or card_type == "newCard_2":
        return "voterid"

    # PAN
    loc1 = ia.find_word_location(doc, 'govt')
    loc2 = ia.find_word_location(doc, 'ofindia')
    loc3 = ia.find_word_location(doc, 'incometaxdepartment')
    loc4 = ia.find_word_location(doc, 'permanentaccountnumber')
    if loc1 is not None and loc2 is not None and loc3 is not None and loc4 is not None:
        return "pan"

    # Driving License
    loc1 = ia.find_word_location(doc, 'driving')
    loc2 = ia.find_word_location(doc, 'name')
    loc3 = ia.find_word_location(doc, 'valid')
    loc4 = ia.find_word_location(doc, 'licence')
    loc5 = ia.find_word_location(doc, 'india')
    if (loc1 is not None or loc4 is not None) and (loc3 is not None or loc2 is not None) and loc5 is not None:
        return "drivinglicence"

    # Passport
    loc1 = ia.find_word_location(doc, 'republicofindia')
    loc2 = ia.find_word_location(doc, 'countrycode')
    loc3 = ia.find_word_location(doc, 'passport')
    loc4 = ia.find_word_location(doc, 'nationality')
    if loc1 is not None and loc2 is not None and loc3 is not None and loc4 is not None:
        return "passport"


def move_to_folder(doc, img_path):
    try:
        doc_typ = get_doc_type(doc)
    except Exception:
        doc_typ = ""
    if doc_typ == "cheque":
        try:
            if not os.path.isdir("./Cheques"):
                os.mkdir("Cheques")
            shutil.move(img_path, "./Cheques/.")
        except Exception:
            pass
    elif doc_typ == "passbook":
        try:
            if not os.path.isdir("./Passbooks"):
                os.mkdir("Passbooks")
            shutil.move(img_path, "./Passbooks/.")
        except Exception:
            pass
    elif doc_typ == "aadhaar":
        try:
            if not os.path.isdir("./Aadhaar"):
                os.mkdir("Aadhaar")
            shutil.move(img_path, "./Aadhaar/")
        except Exception:
            pass
    elif doc_typ == "voterid":
        try:
            if not os.path.isdir("./VoterID"):
                os.mkdir("VoterID")
            shutil.move(img_path, "./VoterID/")
        except Exception:
            pass
    elif doc_typ == "pan":
        try:
            if not os.path.isdir("./PAN"):
                os.mkdir("PAN")
            shutil.move(img_path, "./PAN/")
        except Exception:
            pass
    elif doc_typ == "drivinglicence":
        try:
            if not os.path.isdir("./DrivingLicence"):
                os.mkdir("DrivingLicence")
            shutil.move(img_path, "./DrivingLicence/")
        except Exception:
            pass
    elif doc_typ == "passport":
        try:
            if not os.path.isdir("./Passport"):
                os.mkdir("Passport")
            shutil.move(img_path, "./Passport/")
        except Exception:
            pass
    return doc_typ


img = "E:/justin/DOC_identifier/docs_imgs/"  # folder that contains test imgs.

for filename in os.listdir(img):
    print(filename)
    res, document, txt = wr.data_retrieve(img+filename)
    a = move_to_folder(document, img+filename)
    print(a)
    print("-------------------------------")
