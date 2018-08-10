#!/usr/bin/python -tt'

import sys

def get_exp(filename):
  expense_dic = {}
  total_expense = 0
  exp_perperson = 0
  input_file = open(filename,'r')
  for line in input_file:
    words = line.split()
    words[0] = words[0].lower()
    if words[0] in expense_dic:
     expense_dic[words[0]] = expense_dic[words[0]] + int(words[1])
     total_expense = total_expense + int(words[1]) 
    else:
     expense_dic[words[0]] = int(words[1])
     total_expense = total_expense + int(words[1])
  exp_perperson = total_expense/len(expense_dic)
  for person in expense_dic:
    expense_dic[person] = expense_dic[person] - exp_perperson  
  return expense_dic,total_expense,exp_perperson


def print_exp(filename1,filename2):
  exp_dec_cm,total_exp_cm,exp_perperson_cm = get_exp(filename1)
  exp_dec_dr,total_exp_dr,exp_perperson_dr = get_exp(filename2)
  print "----------- Common Expense -------------------\n"
  print "Total expense is ",total_exp_cm
  print "Expense per person is ",exp_perperson_cm
  print ""
  print "----------- Drinking Expense -----------------\n"
  print "Total expense is ",total_exp_dr
  print "Expense per person is ",exp_perperson_dr  
  print ""
  print "----------- Expense Per Person ----------------\n"
  persons = sorted(exp_dec_cm.keys())
  for person in persons:
    if person in exp_dec_dr:
     exp_dec_cm[person] = exp_dec_cm[person] + exp_dec_dr[person]
    else:
     exp_dec_cm[person] = exp_dec_cm[person]
    print person + '\'s expense is ' + str(exp_dec_cm[person])

     
if __name__ == '__main__':
  print_exp(sys.argv[1],sys.argv[2])