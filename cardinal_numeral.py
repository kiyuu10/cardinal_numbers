import pygame
import time
def tach_ra_list(n):
  """
  dau vao : la mot so integer, khong phai la integer thi khong duoc

  dau ra: la mot list cac so co ba chu so vi du: ['003','456','789']
  ['3','456','789']

  vi du: 123456789 => ['123','456','789']
  """
  str_num = str(n)

  list_contain = ''
  list_of_num = []

  j = 0

  if len(str_num) % 3 == 0:
    i = 0
    while i < len(str_num):
      list_contain += str_num[i]
      j += 1
      if j == 3:
        list_of_num.append(list_contain)
        list_contain = ''
        j = 0
      i += 1
    return list_of_num
  if len(str_num) % 3 == 1:
    str_num = '00' + str_num
    i = 0
    j = 0
    while i < len(str_num):
      list_contain += str_num[i]
      j += 1
      if j == 3:
        list_of_num.append(list_contain)
        list_contain = ''
        j = 0
      i += 1
    while j < len(list_of_num):
      if list_of_num[0][0] == '0' and list_of_num[0][1] == '0':
        list_of_num[0] = list_of_num[0][2]
      j += 1
    return list_of_num

  elif len(str_num) % 3 == 2:
    str_num = '0' + str_num
    i = 0
    j = 0
    while i < len(str_num):
      list_contain += str_num[i]
      j += 1
      if j == 3:
        list_of_num.append(list_contain)
        list_contain = ''
        j = 0
      i += 1
    while j < len(list_of_num):
      if list_of_num[0][0] == '0':
        list_of_num[0] = list_of_num[0][1] + list_of_num[0][2]
      j += 1
    return list_of_num

# print(tach_ra_list(12123005006))

def doi_qua_don_vi(n):
  """
  dau vao la mo so integer
  dau ra la chu cua so do
  vi du : 2 => 'hai'
  """
  row_don_vi = {1 : " một", 2: " hai", 3: " ba" , 4: " bốn ", 5: " lăm", 6: " sáu", 7: " bảy", 8: " tám", 9: " chín"}

  result =''
  for i in row_don_vi:
    if n == i:
      result = row_don_vi[i]
  return result


def doi_qua_hang_chuc(n, region):
  """
  dau vao : la mot so integer, khong phai la integer thi khong duoc

  dau ra: la chu so hang chuc, giong nhu cach doc so ma duoc dua vao o dau vao

  vi du: 23 => "hai mươi ba"
  """
  row_don_vi1 = {1 : "một", 2: "hai", 3: "ba" , 4: "bốn ", 5: "năm", 6: "sáu", 7: "bảy", 8: "tám", 9: "chín"}
  row_don_vi_k = {1 : "mốt", 2: "hai", 3: "ba" , 4: "bốn ", 5: "lăm", 6: "sáu", 7: "bảy", 8: "tám", 9: "chín"}
  row_don_vi = {1 : "một", 2: "hai", 3: "ba" , 4: "bốn ", 5: "lăm", 6: "sáu", 7: "bảy", 8: "tám", 9: "chín"}

  row_chuc_bac = {1 : " mười ", 2: " hai mươi ", 3: " ba mươi " , 4: " bốn mươi ", 5: " năm mươi ", 6: "sáu mươi ", 7: " bảy mươi ", 8: " tám mươi ", 9: " chín mươi ", 0: "linh "}

  row_chuc_nam = {1 : " mười ", 2: "hai mươi ", 3: "ba mươi " , 4: "bốn mươi ", 5: "năm mươi ", 6: " sáu mươi ", 7: " bảy mươi ", 8: " tám mươi ", 9: " chín mươi ", 0: "lẻ "}

  chuc = n // 10
  don_vi = n % 10

  result_don_vi = ''
  result_chuc = ''
  if region == 'north':
    if chuc == 0:
      for i in row_don_vi1:
        if don_vi == i:
          result_don_vi += row_don_vi1[i]
    elif chuc == 1:
      for i in row_don_vi:
        if don_vi == i:
          result_don_vi += row_don_vi[i]
    elif chuc > 1:
      for i in row_don_vi_k:
        if don_vi == i:
          result_don_vi += row_don_vi_k[i]
    for i in row_chuc_bac:
      if chuc == i:
        result_chuc += row_chuc_bac[i]

    result = result_chuc + result_don_vi
    return result
  elif region == 'south':
    if chuc == 0:
      for i in row_don_vi1:
        if don_vi == i:
          result_don_vi += row_don_vi1[i]
    elif chuc == 1:
      for i in row_don_vi:
        if don_vi == i:
          result_don_vi += row_don_vi[i]
    elif chuc > 1:
      for i in row_don_vi_k:
        if don_vi == i:
          result_don_vi += row_don_vi_k[i]
    for i in row_chuc_nam:
      if chuc == i:
        result_chuc += row_chuc_nam[i]

    result = result_chuc + result_don_vi
    return result



def doi_qua_hang_tram(n, region):
  """
  dau vao : la mot so integer, khong phai la integer thi khong duoc

  dau ra: la chu so hang tram, giong nhu cach doc so ma duoc dua vao o dau vao

  vi du: 123 => "mot tram hai mươi ba"
  """
  row_tram ={1 : "một trăm ", 2: "hai trăm ", 3: "ba trăm " , 4: "bốn trăm ", 5: "năm trăm ", 6: "sáu trăm ", 7: "bảy trăm ", 8: "tám trăm ", 9: "chín trăm "}

  list_num = [100,200,300,400,500,600,700,800,900]

  result_tram = ''

  hang_tram = n // 100
  hang_chuc = n % 100

  if n in list_num:
    for i in row_tram:
      if hang_tram == i:
        result_tram += row_tram[i]
    result = result_tram
    return result

  result_chuc = doi_qua_hang_chuc(hang_chuc, region)

  for i in row_tram:
    if hang_tram == i:
      result_tram += row_tram[i]
  result = result_tram + result_chuc

  return result



def doi_qua_chu(list_num, region):
  """
  dau vao: la mot danh sach so da duoc tach ra va dua vao mot list

  vi du nhu : ['123','456','789'] => ['mot tram hai mươi ba','bon tram nam mươi sau', 'bay tram tam mươi chin']

  dau ra: la danh sach cac chu da duoc doi tu danh so duoc dua vao

  vi du: ['123','405','715'] => ['mot tram hai mươi ba','bon tram nam mươi sau', 'bay tram tam mươi chin']
  """

  if region == 'north':
    for j in range(len(list_num)):
      if (list_num[j][0] == '0' and list_num[j][1] == '0') and list_num[j][2] != '0':
        so_ba = int(list_num[j][2])
        so_cuoi = doi_qua_don_vi(so_ba)
        tmp = ' không trăm linh'+so_cuoi
        list_num[j] = tmp
      elif list_num[j][0] == '0' and list_num[j][1] == '0' and list_num[j][2] == '0':
        list_num[j] = 'khong'
      elif list_num[j][0] == '0':
        hai_so = list_num[j][1] + list_num[j][2]
        hai_so_cuoi = doi_qua_hang_chuc(int(hai_so), region)
        tmp = 'không trăm ' + hai_so_cuoi
        list_num[j] = tmp
      else:
        ba_so = int(list_num[j])
        list_num[j] = doi_qua_hang_tram(ba_so, region)
      j+=1
    return list_num
  elif region == 'south' :
    for j in range(len(list_num)):
      if (list_num[j][0] == '0' and list_num[j][1] == '0') and list_num[j][2] != '0':
        so_ba = int(list_num[j][2])
        so_cuoi = doi_qua_don_vi(so_ba)
        tmp = ' không trăm lẻ'+so_cuoi
        list_num[j] = tmp
      elif list_num[j][0] == '0' and list_num[j][1] == '0' and list_num[j][2] == '0':
        list_num[j] = 'khong'
      elif list_num[j][0] == '0':
        hai_so = list_num[j][1] + list_num[j][2]
        hai_so_cuoi = doi_qua_hang_chuc(int(hai_so), region)
        tmp = 'không trăm ' + hai_so_cuoi
        list_num[j] = tmp
      else:
        ba_so = int(list_num[j])
        list_num[j] = doi_qua_hang_tram(ba_so, region)
      j+=1
    return list_num





def ghep_chu(list_chu, region):
  """
  dau vao: la mot danh sach cac chu

  dau ra: la mot chuoi hoan chinh da duoc ghep tu cac chu duoc dua vao

  vi du: ['mot tram hai mươi ba','bon tram nam mươi sau', 'bay tram tam mươi chin'] => 'mot tram hai mươi ba trieu bon tram nam mươi sau nghin bay tram tam mươi chin'
  """
  for i in list_chu:
    if str(i) == 'không trăm linh ':
      i = 'khong'
    elif str(i) == 'không trăm lẻ ':
      i = 'khong'

  leng = len(list_chu)
  for i in list_chu[0]:
    if i == 'l':
      cat = list_chu[0].split()
      if cat[0] == 'linh':
        cat = cat[1]
        list_chu[0] = cat
      elif cat[0] == 'lẻ':
        cat = cat[1]
        list_chu[0] = cat

  ty = ''
  trieu = ''
  nghin = ''
  tram = ''
  if region == 'south':
    if leng == 4:
      if str(list_chu[1]) == 'khong' and str(list_chu[2]) == 'khong' and list_chu[3] == 'khong':
        ty += str(list_chu[0]) + ' tỷ'
        return ty
      elif str(list_chu[1]) == 'khong' and str(list_chu[2]) == 'khong':
        ty += str(list_chu[0]) + ' tỷ ' + str(list_chu[3])
        return ty
      elif str(list_chu[2]) == 'khong' and str(list_chu[3]) == 'khong':
        ty += str(list_chu[0]) + ' tỷ ' + str(list_chu[1]) + ' triệu '
        return ty
      elif str(list_chu[3]) == 'khong':
        ty += str(list_chu[0]) + ' tỷ ' + str(list_chu[1]) + ' triệu ' + str(list_chu[2]) + ' ngàn '
        return ty
      elif str(list_chu[2]) == 'khong' :
        ty += str(list_chu[0]) + ' tỷ ' + str(list_chu[1]) + ' triệu ' + str(list_chu[3])
        return ty
      elif str(list_chu[1]) == 'khong':
        ty += str(list_chu[0]) + ' tỷ ' + str(list_chu[2]) + ' ngàn ' + str(list_chu[3])
        return ty
      else:
        ty += str(list_chu[0]) + ' tỷ ' + str(list_chu[1]) + ' triệu ' + str(list_chu[2]) + ' ngàn ' + str(list_chu[3])
        return ty
    elif leng == 3:

      if str(list_chu[1]) == 'khong' and str(list_chu[2]) == 'khong':
        trieu += str(list_chu[0]) + 'triệu'
        return trieu

      elif str(list_chu[1]) == 'khong':
        trieu += str(list_chu[0]) + 'triệu' + str(list_chu[2])
        return trieu
      elif str(list_chu[2]) == 'khong':
        trieu += str(list_chu[0]) + 'triệu' + str(list_chu[1]) + ' ngàn '
        return trieu
      else:
        trieu += str(list_chu[0]) + ' triệu ' + str(list_chu[1])  + ' ngàn ' + str(list_chu[2])
        return trieu
    elif leng == 2:
      if str(list_chu[1]) == 'khong':
        nghin += str(list_chu[0]) + ' ngàn '
        return nghin
      else:
        nghin += str(list_chu[0]) + ' ngàn ' + str(list_chu[1])
      return nghin
    else:
      tram += list_chu[0]
      return tram
  elif region == 'north':
    if leng == 4:
      if str(list_chu[1]) == 'khong' and str(list_chu[2]) == 'khong' and list_chu[3] == 'khong':
        ty += str(list_chu[0]) + ' tỷ '
        return ty
      elif str(list_chu[1]) == 'khong' and str(list_chu[2]) == 'khong':
        ty += str(list_chu[0]) + ' tỷ ' + str(list_chu[3])
        return ty
      elif str(list_chu[2]) == 'khong' and str(list_chu[3]) == 'khong':
        ty += str(list_chu[0]) + ' tỷ ' + str(list_chu[1]) + ' triệu '
        return ty
      elif str(list_chu[3]) == 'khong':
        ty += str(list_chu[0]) + ' tỷ ' + str(list_chu[1]) + ' triệu ' + str(list_chu[2]) + ' nghìn '
        return ty
      elif str(list_chu[2]) == 'khong' :
        ty += str(list_chu[0]) + ' tỷ ' + str(list_chu[1]) + ' triệu ' + str(list_chu[3])
        return ty
      elif str(list_chu[1]) == 'khong':
        ty += str(list_chu[0]) + ' tỷ ' + str(list_chu[2]) + ' nghìn ' + str(list_chu[3])
        return ty
      else:
        ty += str(list_chu[0]) + ' tỷ ' + str(list_chu[1]) + ' triệu ' + str(list_chu[2]) + ' nghìn ' + str(list_chu[3])
        return ty
    elif leng == 3:

      if str(list_chu[1]) == 'khong' and str(list_chu[2]) == 'khong':
        trieu += str(list_chu[0]) + 'triệu'
        return trieu

      elif str(list_chu[1]) == 'khong':
        trieu += str(list_chu[0]) + ' triệu ' + str(list_chu[2])
        return trieu
      elif str(list_chu[2]) == 'khong':
        trieu += str(list_chu[0]) + ' triệu ' + str(list_chu[1]) + ' nghìn '
        return trieu
      else:
        trieu += str(list_chu[0]) + ' triệu ' + str(list_chu[1])  + ' nghìn ' + str(list_chu[2])
        return trieu
    elif leng == 2:
      if str(list_chu[1]) == 'khong':
        nghin += str(list_chu[0]) + ' nghìn '
        return nghin
      else:
        nghin += str(list_chu[0]) + ' nghìn ' + str(list_chu[1])
      return nghin
    else:
      tram += list_chu[0]
      return tram

def change_one(n):
  """
  dau vao la mo so integer
  dau ra la chu cua so do
  vi du : 2 => 'hai'
  """
  row_don_vi = {1 : "one", 2: "two", 3: "three" , 4: "four ", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

  result =''
  for i in row_don_vi:
    if n == i:
      result = row_don_vi[i]
  return result


def change_ten(n):
  """
  dau vao : la mot so integer, khong phai la integer thi khong duoc

  dau ra: la chu so hang chuc, giong nhu cach doc so ma duoc dua vao o dau vao

  vi du: 23 => "hai mươi ba"
  """

  row_don_vi = {1 : "one", 2: "two", 3: "three" , 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

  row_chuc = {1 : "ten", 2: "twenty-", 3: "thirty-" , 4: "fourty-", 5: "fifty-", 6: "sixty-", 7: "seventy-", 8: "eighty-", 9: "ninety-"}

  row_chuc_2 = { 11 : "eleven ", 12 : "twelve ", 13 : "thirteen ", 14: "fourteen ", 15: "fifteen ", 16: "sixteen ", 17: "seventeen", 18: "eighteen", 19: "nineteen"}

  chuc = n // 10
  don_vi = n % 10

  row_chuc_3 = {10 : "ten", 20: "twenty", 30: "thirty" , 40: "fourty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}

  result_don_vi = ''
  result_chuc = ''
  for i in row_chuc_3:
    if n == i:
      result_chuc = row_chuc_3[i]
      return result_chuc

  for i in row_don_vi:
    if don_vi == i:
      result_don_vi += row_don_vi[i]
  if n >= 11 and n <= 19:
    for i in row_chuc_2:
      if n == i:
        result_chuc += row_chuc_2[i]
        return result_chuc
  else:
    for i in row_chuc:
      if chuc == i:
        result_chuc += row_chuc[i]

  result = result_chuc + result_don_vi
  return result

# print(doi_qua_hang_chuc(96))

def change_hundred(n):
  """
  dau vao : la mot so integer, khong phai la integer thi khong duoc

  dau ra: la chu so hang tram, giong nhu cach doc so ma duoc dua vao o dau vao

  vi du: 123 => "mot tram hai mươi ba"
  """
  row_tram ={1 : "one hundred", 2: "two hundred", 3: "three hundred" , 4: "four hundred", 5: "five hundred", 6: "six  hundred", 7: "seven hundred", 8: "eight hundred", 9: "nine hundred"}

  list_num = [100,200,300,400,500,600,700,800,900]

  result_tram = ''

  hang_tram = n // 100
  hang_chuc = n % 100

  if n in list_num:
    for i in row_tram:
      if hang_tram == i:
        result_tram += row_tram[i]
    result = result_tram
    return result

  result_chuc = change_ten(hang_chuc)

  for i in row_tram:
    if hang_tram == i:
      result_tram += row_tram[i]
  result = result_tram + ' and '+ result_chuc

  return result



def change_to_text(list_num):
  """
  dau vao: la mot danh sach so da duoc tach ra va dua vao mot list

  vi du nhu : ['123','456','789'] => ['mot tram hai mươi ba','bon tram nam mươi sau', 'bay tram tam mươi chin']

  dau ra: la danh sach cac chu da duoc doi tu danh so duoc dua vao

  vi du: ['123','405','715'] => ['mot tram hai mươi ba','bon tram nam mươi sau', 'bay tram tam mươi chin']
  """

  for j in range(len(list_num)):
    if (list_num[j][0] == '0' and list_num[j][1] == '0') and list_num[j][2] != '0':
      so_ba = int(list_num[j][2])
      so_cuoi = change_one(so_ba)
      list_num[j] = so_cuoi
    elif list_num[j][0] == '0' and list_num[j][1] == '0' and list_num[j][2] == '0':
      list_num[j] = 'khong'
    elif list_num[j][0] == '0':
      hai_so = list_num[j][1] + list_num[j][2]
      hai_so_cuoi = change_ten(int(hai_so))
      list_num[j] = hai_so_cuoi
    else:
      ba_so = int(list_num[j])
      list_num[j] = change_hundred(ba_so)
    j+=1
  return list_num




def join_text(list_chu):
  """
  dau vao: la mot danh sach cac chu

  dau ra: la mot chuoi hoan chinh da duoc ghep tu cac chu duoc dua vao

  vi du: ['mot tram hai mươi ba','bon tram nam mươi sau', 'bay tram tam mươi chin'] => 'mot tram hai mươi ba trieu bon tram nam mươi sau nghin bay tram tam mươi chin'
  """


  leng = len(list_chu)
  for i in list_chu[0]:
    if i == 'a':
      cat = list_chu[0].split()
      if cat[0] == 'and':
        cat = cat[1]
        list_chu[0] = cat

  ty = ''
  trieu = ''
  nghin = ''
  tram = ''
  if leng == 4:
    # [000,000,000,000]
    if str(list_chu[1]) == 'khong' and str(list_chu[2]) == 'khong' and list_chu[3] == 'khong':
      ty += str(list_chu[0]) + ' billion '
      return ty
    elif str(list_chu[1]) == 'khong' and str(list_chu[2]) == 'khong':
      ty += str(list_chu[0]) + ' billion ' + str(list_chu[3])
      return ty
    elif str(list_chu[2]) == 'khong' and str(list_chu[3]) == 'khong':
      ty += str(list_chu[0]) + ' billion ' + str(list_chu[1]) + ' million '
      return ty
    elif str(list_chu[3]) == 'khong':
      ty += str(list_chu[0]) + ' billion ' + str(list_chu[1]) + ' million ' + str(list_chu[2]) + ' thousand '
      return ty
    elif str(list_chu[2]) == 'khong' :
      if len(list_chu[3]) <= 5:
        ty += str(list_chu[0]) + ' billion ' + str(list_chu[1]) + ' million and ' + str(list_chu[3])
        return ty
      else:
        ty += str(list_chu[0]) + ' billion ' + str(list_chu[1]) + ' million, ' + str(list_chu[3])
        return ty
    elif str(list_chu[1]) == 'khong':
      ty += str(list_chu[0]) + ' billion ' + str(list_chu[2]) + ' thousand ' + str(list_chu[3])
      return ty
    else:
      ty += str(list_chu[0]) + ' billion ' + str(list_chu[1]) + ' million ' + str(list_chu[2]) + ' thousand ' + str(list_chu[3])
      return ty
  elif leng == 3:

    if str(list_chu[1]) == 'khong' and str(list_chu[2]) == 'khong':
      trieu += str(list_chu[0]) + ' million '
      return trieu

    elif str(list_chu[1]) == 'khong':
      trieu += str(list_chu[0]) + ' million ' + str(list_chu[2])
      return trieu
    elif str(list_chu[2]) == 'khong':
      trieu += str(list_chu[0]) + ' million ' + str(list_chu[1]) + ' thousand '
      return trieu
    else:
      trieu += str(list_chu[0]) + ' million ' + str(list_chu[1])  + ' thousand ' + str(list_chu[2])
      return trieu
  elif leng == 2:
    if str(list_chu[1]) == 'khong':
      nghin += str(list_chu[0]) + ' thousand '
      return nghin
    else:
      nghin += str(list_chu[0]) + ' thousand ' + str(list_chu[1])
    return nghin
  else:
    tram += list_chu[0]
    return tram




def integer_to_english_numeral(number_integer, activate_tts = False):
  type_num = isinstance(number_integer, int)

  if not type_num == True:
    raise TypeError('Not an integer')
  elif number_integer < 0:
    raise ValueError('Not a positive integer')

  str_num = str(number_integer)
  if len(str_num) > 12:
    raise TypeError('Not an integer')

  tach = tach_ra_list(number_integer)

  chu = change_to_text(tach)

  result = join_text(chu)
  if activate_tts == False and activate_tts == None:
    return result
  else:
    pygame.mixer.init()
    print(result)
    result = result.replace("-", " ")
    cat = result.split()
    for i in cat :
      pygame.mixer.music.load('./eng-US/'+i+'.ogg')
      pygame.mixer.music.play()
      time.sleep(0.6)

def integer_to_vietnamese_numeral(number_integer, region = 'north', activate_tts = False):

  type_num = isinstance(number_integer, int)

  if not type_num == True:
    raise TypeError('Not an integer')
  elif number_integer < 0:
    raise ValueError('Not a positive integer')

  str_num = str(number_integer)
  if len(str_num) > 12:
    raise TypeError('Not an integer')

  tach = tach_ra_list(number_integer)

  chu = doi_qua_chu(tach, region)


  result = ghep_chu(chu, region)

  if activate_tts == False and activate_tts == None:
    return result
  else:
    pygame.mixer.init()
    print(result)
    if region == 'north':
      cat = result.split()
      for i in cat:
        pygame.mixer.music.load('./north/'+i+'.ogg')
        pygame.mixer.music.play()
        time.sleep(0.6)
    else:
      cat = result.split()
      for i in cat:
        pygame.mixer.music.load('./south/'+i+'.ogg')
        pygame.mixer.music.play()
        time.sleep(0.6)

print(integer_to_english_numeral(123456, activate_tts = True))
print(integer_to_vietnamese_numeral(999999999999, region = 'north', activate_tts = True))
