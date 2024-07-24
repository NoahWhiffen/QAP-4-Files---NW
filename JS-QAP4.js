// QAP 4 - Introduction to Javascript

// Motel Customer Object

let motelCustomer = new Object();
motelCustomer.name = "John Smith"
motelCustomer.gender = "Male";
motelCustomer.birthDate = "1998-07-30";
motelCustomer.birthDate = new Date(motelCustomer.birthDate)
motelCustomer.roomPref = ["Non-smoking", "Queen Bed"];
motelCustomer.payMethod = "Visa";
motelCustomer.mail = { // Sub-Object
    street: "123 Water Street",
    city: "St. John's",
    province: "NL",
    postCode: "A1A 1A1",
};
motelCustomer.phoneNum = "1-709-766-5656";
motelCustomer.checkIn = "2024-07-19";
motelCustomer.checkIn = new Date(motelCustomer.checkIn);
motelCustomer.checkOut = "2024-07-25";
motelCustomer.checkOut = new Date(motelCustomer.checkOut);



const descriptionElement = document.getElementById("description");
const description = customer.customerDesc();
descriptionElement.innerHTML = `<p>${description}</p>`