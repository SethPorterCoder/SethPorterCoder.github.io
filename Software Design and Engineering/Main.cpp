#include <string>
#include <iostream>
#include <iostream>
#include <fstream>
#include <vector>
#include <string.h>;



using namespace std;
//Input for switches because switches do not allow variable declarations
string switchInput() {
	string input = "";
	cin >> input;
	return input;
}

void main() {
	//Initializing two vectors fpr easier parsing
	vector<string> counts{};
	vector<string> searcher{};
	ifstream file("CS210_Project_Three_Input_File.txt");

	string line = "";

	//Buffering through the file to find all of the unique words
	if (file.is_open()) {
		getline(file, line);
		searcher.push_back(line);

		while (file >> line) {
			for (int i = 0; i < searcher.size(); i++) {
				if (i == (searcher.size() - 1) && line != searcher[i]) {
					searcher.push_back(line);
				}
				else if (line == searcher[i]) {
					break; //Break the for loop if we find a match
				}
			}
		}
	}
	//Create a vector for a stored unique words
	for (int i = 0; i < searcher.size(); i++) {
		counts.push_back(searcher[i]);
		counts.push_back("0");
	}

	//Reset file poiter easy way
	file.close();
	file.open("CS210_Project_Three_Input_File.txt");

	if (file.is_open()) {
		for (int i = 0; i < counts.size(); i = i + 2) {
			while (file >> line) {
				if (counts[i] == line) {
					counts[i + 1] = to_string(stoi(counts[i + 1]) + 1);
				}
			}
			//Reset file poiter easy way
			file.close();
			file.open("CS210_Project_Three_Input_File.txt");
		}
	}

	file.close();

	bool loop = true;
	//Menu infinite loop
	while (loop) {
		string option = "";
		cout << "Chada Tech File Checker" << endl;
		cout << "-----------------------" << endl;
		cout << "1. Find a word's count" << endl;
		cout << "2. Print all word's and their frequency" << endl;
		cout << "3. Print all word's and their frequency displayed in asterisks" << endl;
		cout << "4. Exit program" << endl;

		cout << endl << "Enter a number" << endl;
		//Using switch statements beacuse they run faster than a if-else tree
		//Using try catch and stoi function just in case the user enters a non number
		string input = "";
		int counter = -1;
		try {
			cin >> option;
			switch (stoi(option)) {
			case 1:
				cout << "Enter a word to search" << endl;
				input = switchInput();
				for (int i = 0; i < counts.size(); i = i + 2) {
					if (input == counts[i]) {
						counter = stoi(counts[i + 1]);
					}
				}

				if (counter == -1) {
					cout << "Word was not found" << endl;
				}
				else {
					cout << input << " " << counter;
				}
				break;
			case 2:
				for (int i = 0; i < counts.size(); i = i + 2) {
					cout << counts[i] << " " << counts[i + 1] << endl;
				}
				cout << endl;
				break;
			case 3:
				for (int i = 0; i < counts.size(); i = i + 2) {
					cout << counts[i] << " ";

					for (int x = 0; x < stoi(counts[i + 1]); x++) {
						cout << "*";
					}

					cout << endl;
				}
				break;
			case 4:
				cout << "Goodbye" << endl;
				loop = false;
				break;
			default: 
				cout << "Invalid input";
				break;
			}
		}
		catch (...) {
			cout << "Invalid input";
		}

		cout << endl;
	}

}

