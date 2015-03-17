#include <iostream>
#include <string>

using namespace std;

class FlashCard {
private:
	string question;
	string answer;

public:
	FlashCard() {
		question = "";
		answer = "";
	}
	FlashCard(const char* q, const char* ans ) {
		question = q;
		answer = ans;
	}
	void setQuestion(const char* q) {
		question = q;
	}
	void setAnswer(const char* a) {
		answer = a;
	}
	string getQuestion() {
		return question;
	}
	string getAnswer() {
		return answer;
	}

	bool checkAnswer(string response) {
		return answer == response;
	}

	bool checkAnswer(const char *response) {
		return answer == response;
	}

};

int main(int argc, char const *argv[])
{
	FlashCard fc1("1+1","2");
	cout << "Question: " << fc1.getQuestion() << endl;
	string input;
	cin >> input;
	if (fc1.checkAnswer(input)) {
		cout << "Correct!" << endl;
	} else {
		cout << "Incorrect" << endl;
	}

	cout << fc1.getQuestion() << " = " << fc1.getAnswer() << endl;
	return 0;
}