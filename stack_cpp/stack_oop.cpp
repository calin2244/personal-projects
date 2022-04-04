#include <iostream>
#include <vector>

#define SIZE 100000
//const unsigned int SIZE = 100;

class stack{
    int stck[SIZE];
    int pos;
    public:
        stack();
        void push(int i);
        int pop();
        int size() const{
            return pos;
        }
        int getElementAtPosition(int i);
        void showStackElements();
        stack operator+(stack& other)
        {
            stack myStack;
            for(int i = 0; i<other.size(); i++)
            {
                (*this).push(other.getElementAtPosition(i));
            }

            for(int i = 0; i<(*this).size(); i++)
            {
                myStack.push((*this).getElementAtPosition(i));
            }
            //std::cout<<myStack.size();
            //myStack.showStackElements();
            return myStack;
        }
};

int main()
{
    //simple operations of adding elements and combining the first two stacks
    stack stack1, stack2, stackTree;
    stack1.push(4);
    stack1.push(6);
    stack2.push(7);
    stack2.push(9);
    stackTree = stack1 + stack2;
    stackTree.showStackElements();
    //stackTree.showStackElements();
    
}

void stack::push(int i)
{
    if(pos == SIZE)
    {
        std::cout<<"Stack overflow\n";
        return;
    }
    
    stck[pos++] = i;
}

int stack::pop()
{
    if(pos == 0)
    {
        std::cout<<"Stack underflow";
        return 0;
    }
    pos--;
    return stck[pos];
}

void stack::showStackElements()
{
    if(pos == 0)
    {
        std::cout<<"Stack underflow\n";
        return;
    }
    for(int i = 0; i < stack::size(); ++i)
        std::cout<<stck[i]<<" ";
    std::cout<<'\n';
}

int stack::getElementAtPosition(int i)
{
    if(i > pos)
    {
        std::cout<<"Nu exista, out of bounds\n";
        return 0;
    }
    return stck[i];
}

stack::stack(){
    pos = 0;
}
