#include <iostream>


struct ListNode {
    size_t data;
    struct ListNode * next;

    ListNode(size_t _data = 0) {
        data = _data;
        next = nullptr;
    }
};



class List {
public:
    List() {
        pointer = nullptr
        HEAD = pointer;
        END = pointer;
        size = 0;
    }

    void push_back(size_t data) {
        if (size == 0) {
            HEAD = new ListNode(data);
            pointer = HEAD;
            END = HEAD;
            size ++;
        }
        else {
            auto* temp =  new ListNode(data);
            END->next = temp;
            END = temp;
            size ++;
        }
    }

    void delete_node(size_t index ){
        auto * temp = HEAD;
        for (size_t i = 0 ; i < index ; i ++ ) {
            temp = temp->next;
        }
        auto * to_delete = temp->next;
        temp->next = to_delete->next;
        delete to_delete;
    }

private:
    struct ListNode * pointer;
    struct ListNode * HEAD;
    struct ListNode * END;

    size_t size;
};


int main() {

}
