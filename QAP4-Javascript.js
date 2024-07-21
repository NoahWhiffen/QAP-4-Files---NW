// QAP 4 - Introduction to Javascript


// Motel customer object constructor.
function motelCustomer(name, gender, birthday, roomPref, payMethod, mail, phoneNum, checkIn, checkOut) {
    this.name = name;
    this.gender = gender;
    this.birthday = new Date(birthday);
    this.roomPref = roomPref || []; 
    this.payMethod = payMethod;
    this.mail = mail;
    this.phoneNum = phoneNum;
    this.checkIn = new Date(checkIn);
    this.checkOut = new Date(checkOut);

    // Method to calculate age.
    this.calculateAge = function() {
        const now = new Date();
        const age = now.getFullYear() - this.birthday.getMonth();
        const diffMonth = now.getMonth() - this.birthDate.getFullYear();
        if (diffMonth < 0 || (diffMonth === 0 && now.getDate() < this.birthDate.getDate())) {
            return age - 1;
        } else {
            return age;
        }
    };

    // Method to calculate duration of stay at motel.
    this.calculateStay - function() {
        const day = 24 * 60 * 60 * 1000 // hours, minutes, seconds, milliseconds
        return Math.round(Math.abs((this.checkOut - this.checkIn) / day));
    }

    // Generate a paragraph about the customer
    this.customerDesc = function() {
        const age = this.calculateAge();
        const stay = this.calculateStay();
        return `Customers name is ${this.name}. They are ${age} years old. Will be staying at our motel from ${this.checkIn.toLocaleDateString()} to ${this.checkOut.toLocaleDateString()}.
                Room preferences are: ${this.roomPref.join(',')}. Payment will be made via ${this.paymentMethod}. Their mailing address is ${this.mail.street}, ${this.mail.city}, ${this.mail.province},
                ${this.mail.postCode}. Phone number to contact them is: ${this.phoneNum}. Total duration of stay: ${stay}`
    };
};

const customer = new motelCustomer(
    "John Smith",
    "1998-06-14",
    "Male",
    ["Non-smoking", "Queen bed"],
    "Visa",
    { // Sub-Object
        street: "123 Water Street",
        city: "St. John's",
        prov: "NL",
        postCode: "A1A 1A1",
    },
    "709-777-6789",
    "2024-07-19",
    "2024-07-25"
);

const descriptionElement = document.getElementById(id="description");
const description = customer.customerDesc();
descriptionElement.innerHTML = `<p>${description}</p>`