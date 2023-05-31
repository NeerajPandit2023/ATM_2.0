import atmTool 
for i in range(100):
    print('\t\t\tWelcome in Bank of India\n\t\t\tInsert your Debit card details.')
    pin=int(input('Enter your pin: '))
    x=atmTool.check_pin(pin)
    if pin==x:
        detail=atmTool.detail(x)
        print(detail)
        for k in range(5):
            c=input('choose your tarnsaction\n1. Withdraw\n2. Balance enqueiry\n3. fast cash\n4. Credit Amount\n: ')
            if c=='1':
                withdraw_am=int(input('Enter your widthdraw amount: '))
                avl_bal=atmTool.balance(x)
                if (withdraw_am==avl_bal or withdraw_am<avl_bal) and withdraw_am%100==0:
                    up_bal = avl_bal-withdraw_am
                    w=atmTool.update_bal(up_bal,x)
                    print(w,'Thank you for transaction')
                    print('Please collect cash And Debit Card')
                elif x%100!=0:
                    print("Incorrect Ammount.")
                else:
                    print('>>>Tu garib hai. ! sorry can\'t your withdraw amount\nyour available balance is',n,'only & So you can exit transaction')
                if k!=4:
                    x2=input('If you want to check more operation (yes/no): ')
                    if x2=='no':
                        break
            elif c=='2':
                n=atmTool.balance(x)
                print('Available balance is',n)
                if k!=4:
                    x2=input('If you want to check more operation (yes/no): ')
                    if x2=='no':
                        break
            elif c=='3':
                f=int(input('choose amount 1-1000, 2-500, 3-2000, 4,5000 : '))
                cbal=atmTool.balance(x)
                if f==1 and cbal>1000:
                    uba=cbal-1000
                    l=atmTool.update_bal(uba,x)
                    print('Take cash 1000')
                elif f==2 and cbal>500:
                    uba=cbal-500
                    l=atmTool.update_bal(uba,x)
                    print('Take cash 500')
                elif f==3 and cbal>2000:
                    uba=cbal-2000
                    l=atmTool.update_bal(uba,x)
                    print('Take cash 2000')
                elif f==4 and cbal>5000:
                    uba=cbal-5000
                    l=atmTool.update_bal(uba,x)
                    print('Take cash 5000')
                else:
                    if cbal<f:
                        print('Tu garib hai. Your A/c avl_bal',cbal)
                    else:
                        print('Please Choose your transaction.')
                if k!=4:
                    x2=input('If you want to check more operation (yes/no): ')
                    if x2=='no':
                        break
            elif c=='4':
                add_amt=int(input('Enter Credit amount: '))
                c_bal=atmTool.balance(x)
                u_bal = c_bal+add_amt
                f=atmTool.update_bal(u_bal,x)
                print(f"Credited Rs.{add_amt}. And Your Avl Bal Rs.{u_bal}.")
                if k!=4:
                    x2=input('If you want to check more operation (yes/no): ')
                    if x2=='no':
                        break
            else:
                print('pls choose tansaction.')
        else:
            print('>>>> !! Something went worng! you are done more transaction! So stop here.')
    else:
        print(x)
else:
    print("Today's over transcation")
                