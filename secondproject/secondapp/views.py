from decimal import Decimal
from itertools import product
from django.shortcuts import get_object_or_404, redirect, render
from h11 import Response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse




from secondapp.models import Question, UserData, Product

# Create your views here.
def display(request):
     return render(request,'questionmanagement.html')

def addQuestion(request):
     
      Question.objects.create(qno=request.GET["qno"],qtext=request.GET["qtext"],answer=request.GET["answer"],op1=request.GET["op1"],op2=request.GET["op2"],op3=request.GET["op3"],op4=request.GET["op4"],subject=request.GET["subject"])

      return render(request,'questionmanagement.html',{'message':'Question Added Successfully'})


def viewQuestion(request):

     question=Question.objects.get(qno=request.GET["qno"],subject=request.GET["subject"])

     return render(request,'questionmanagement.html',{'question':question})

def deleteQuestion(request):
      Question.objects.filter(qno=request.GET["qno"],subject=request.GET["subject"]).delete()
      return render(request,'questionmanagement.html',{'message':'record deleted'})


def updateQuestion(request):
     question=   Question.objects.filter(qno=request.GET["qno"],subject=request.GET["subject"])
     question.update(qtext=request.GET['qtext'],answer=request.GET['answer'],op1=request.GET['op1'],op2=request.GET['op2'],op3=request.GET['op3'],op4=request.GET['op4'])

     return render(request,'questionmanagement.html',{'message':'record updated'})

def giveMeRegister(request):
          return render(request,'register.html')

def giveMeLogin(request):
      return render(request,'login.html')


def register(request):

    usernamefrombrowser=request.GET["username"] 
    passfrombrowser=request.GET["password"]
    mobileno=request.GET["mobno"]

    # create method will save given details in database table userdata . it will generate and execute insert query

    UserData.objects.create(username=usernamefrombrowser,password=passfrombrowser,mobno=mobileno)

   # create() will create new row in database table

    #print(connection.queries)

    return render(request,"login.html",{'message':"registration successful . please login now"})



def login(request):
    
    usernamefrombrowser=request.GET["username"] #tka
    passfrombrowser=request.GET["password"] # ttdfdf

    request.session["username"]=usernamefrombrowser

    # {username=tka} session dictionary

    try:
        userfromdatabase=UserData.objects.get(username=usernamefrombrowser) # get() will give object from Database
    except:
        return render(request,"login.html",{'message':"Invalid username"})
    
   # print(connection.queries)
    
    # userfromdatabase==> [username=tka  password=tkakiranacademy mobno=12345] UserData class's object is given by get() method

    if userfromdatabase.password == passfrombrowser:
        
        request.session['answers'] = {}
        request.session['score'] = 0
        request.session["qno"]=-1
       
        # queryset=Question.objects.filter(subject='math').values()
        # listofquestions=list(queryset)
        # request.session["listofquestions"]=listofquestions

        # render(request,"questionnavigation.html",{'message':"welcome " + usernamefrombrowser})
        return render(request,"subject.html",{'message':"welcome " + usernamefrombrowser})

    
    #serilizable
    
    else:

        return render(request,"login.html",{'message':"Invalid password..",'oldusername':usernamefrombrowser})

def startTest(request):
    subjectname=request.GET["subject"]
    request.session['subject']=subjectname
    
    queryset = Question.objects.filter(subject=subjectname).values()
    listofquestions=list(queryset)
    request.session["listofquestions"]=listofquestions

    return render(request,"questionnavigation.html",{'question':listofquestions[0]})

def nextQuestion(request):
    if 'op' in request.GET:

        allanswers=request.session['answers']

        allanswers[request.GET['qno']]=[request.GET['qno'],request.GET['qtext'],request.GET['answer'],request.GET['op']]

        # allanswers  {'1':[1,'what','a','c'],'2' : ['2','why','d','d']}

        print(allanswers)

    
    allquestions=request.session["listofquestions"]

    questionindex=request.session['qno']
    
    if questionindex<len(allquestions)-1:

        request.session["qno"]=request.session["qno"] + 1
    
        print(f"qno is {request.session['qno']}")

        question=allquestions[request.session["qno"]]

    else:

        return render(request,'questionnavigation.html',{'message':"click on previous",'question':allquestions[len(allquestions)-1]})

    return render(request,'questionnavigation.html',{'question':question})

    # qno=qno+1



def previousQuestion(request):
    if 'op' in request.GET:

        allanswers=request.session['answers']

        allanswers[request.GET['qno']]=[request.GET['qno'],request.GET['qtext'],request.GET['answer'],request.GET['op']]

        print(allanswers)

    allquestions=request.session["listofquestions"]
    questionindex=request.session['qno']

    if questionindex>0:

        request.session["qno"]=request.session["qno"] - 1
    
        print(f"qno is {request.session['qno']}")

        question=allquestions[request.session["qno"]]

    else:

        return render(request,'questionnavigation.html',{'message':"click on next",'question':allquestions[0]})

    return render(request,'questionnavigation.html',{'question':question})


def endexam(request):

        if 'op' in request.GET:

            allanswers=request.session['answers'] # {}

            allanswers[request.GET['qno']]=[request.GET['qno'],request.GET['qtext'],request.GET['answer'],request.GET['op']]

            print(allanswers)


        responses=request.session['answers']
        allanswers2=responses.values()
        
        for ans in allanswers2:
        
            print(f'correct answer {ans[2]}  and submitted answer is {ans[3]}') 
            
            if ans[2]==ans[3]:
                    request.session['score']=request.session['score'] + 1

        finalscore=request.session['score']
        print(f'Your score is {finalscore}')        
                
        # try:
        #     Result.objects.create(username=request.session['username'],subject=request.session['subject'],score=finalscore)
        # except:
        #     return render(request,'login.html')    


        return render(request,'score.html',{'score':finalscore,'responses':allanswers2})   

@api_view(['GET'])
def sendData(request):
     return Response({"rno":1,"name":"john"})

@api_view(['GET'])
def getAllUsers(request):
     queryset=UserData.objects.all().values()

     listofusers=list(queryset)

     return Response(listofusers)

@api_view(['GET'])
def getAllquestion(request):
    queryset = Question.objects.all().values()
    listofquestions = list(queryset)
    return Response(listofquestions)

@api_view(['GET'])
def getUser(request,username):
     
     userfromdb=UserData.objects.get(username=username)
     response=Response({'username':userfromdb.username,'password':userfromdb.password,'mobno':userfromdb.mobno})
     return response

@api_view(['POST'])
def addUser(request):
    print(request.data)
    userFromClient=request.data

    UserData.objects.create(username=userFromClient["username"],password=userFromClient["password"],mobno=userFromClient["mobno"])
    response=Response(userFromClient)
    return response

@api_view(['PUT'])
def updateUser(request):
     dictionary=request.data
     userfromdb=UserData.objects.get(username=dictionary["username"])
     userfromdb.password=dictionary["mobno"]
     userfromdb.save()
     return Response(dictionary)

# GET all products
@api_view(['GET'])
def getAllProducts(request):
    products = Product.objects.all()
    data = [
        {
            'product_id': p.product_id,
            'product_name': p.product_name,
            'quantity': p.quantity,
            'price': p.price,
            'image_url': p.image_url
        } for p in products
    ]
    return Response(data)


# GET product by ID
@api_view(['GET'])
def getProduct(request, product_id):
    try:
        product = Product.objects.get(product_id=product_id)
        data = {
            'product_id': product.product_id,
            'product_name': product.product_name,
            'quantity': product.quantity,
            'price': product.price,
            'image_url': product.image_url
        }
        return Response(data)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)


# POST - Add a product with image URL
@api_view(['POST'])
def addProduct(request):
    data = request.data
    Product.objects.create(
        product_name=data['product_name'],
        quantity=data['quantity'],
        price=data['price'],
        image_url=data.get('image_url')  # Optional field
    )
    return Response({'message': 'Product added successfully'}, status=201)


# PUT - Update a product
@api_view(['PUT'])
def updateProduct(request):
    data = request.data
    try:
        product = Product.objects.get(product_id=data['product_id'])
        product.product_name = data['product_name']
        product.quantity = data['quantity']
        product.price = data['price']
        product.image_url = data.get('image_url')  # Optional update
        product.save()
        return Response({'message': 'Product updated successfully'})
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)


# DELETE - Delete a product
@api_view(['DELETE'])
def deleteProduct(request, id):
    try:
        product = Product.objects.get(product_id=id)
        product.delete()
        return Response({'message': 'Product deleted successfully'})
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)




