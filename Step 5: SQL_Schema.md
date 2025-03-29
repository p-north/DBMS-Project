# Library DB Schema

``` sql
--Create Tables
CREATE TABLE IF NOT EXISTS member(
  memberID INTEGER PRIMARY KEY,
  firstName TEXT NOT NULL,
  lastName TEXT NOT NULL,
  dateOfBirth DATE NOT NULL,
  email TEXT NOT NULL,
  phone TEXT NOT NULL,
  address TEXT NOT NULL,
  membershipStart DATE NOT NULL,
  membershipEnd DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS item(
    itemID INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    itemType TEXT NOT NULL,
    author TEXT NOT NULL,
    publisher TEXT,
    publicationYear INTEGER,
    edition INTEGER,
    genre TEXT NOT NULL,
    language TEXT NOT NULL,
    ISBN TEXT NOT NULL,
    availableCopies INTEGER NOT NULL,
    totalCopies INTEGER NOT NULL,
    location TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS personnel(
    employeeID INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    department TEXT NOT NULL,
    hireDate DATE NOT NULL,
    contactInfo TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS borrow_transaction(
    transactionID INTEGER PRIMARY KEY,
    memberID INTEGER NOT NULL,
    itemID INTEGER NOT NULL,
    borrowDate DATE NOT NULL,
    dueDate DATE NOT NULL,
    returnDate DATE,
    fineAmount DECIMAL(10,2),
    FOREIGN KEY (memberID) REFERENCES member (memberID),
    FOREIGN KEY (itemID) REFERENCES item (itemID)
);

CREATE TABLE IF NOT EXISTS fine(
    fineID INTEGER PRIMARY KEY,
    memberID INTEGER NOT NULL,
    transactionID INTEGER NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    issueDate DATE NOT NULL,
    paymentDate DATE,
    FOREIGN KEY (memberID) REFERENCES member (memberID),
     FOREIGN KEY (transactionID) REFERENCES borrow_transaction (transactionID)  
);


CREATE TABLE IF NOT EXISTS room (
    roomId INTEGER PRIMARY KEY,
    roomName TEXT NOT NULL,
    capacity INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS event (
    eventId INTEGER PRIMARY KEY,
    eventName TEXT NOT NULL,
    eventType TEXT,
    description TEXT,
    targetAudience TEXT,
    date DATE NOT NULL,
    startTime TIME NOT NULL,
    endTime TIME NOT NULL,
    roomId INTEGER,
    FOREIGN KEY (roomId) REFERENCES room(roomId)
);

CREATE TABLE IF NOT EXISTS future_item (
    futureItemId INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    itemType TEXT,
    author TEXT,
    expectedArrivalDate DATE,
    status TEXT
);

CREATE TABLE IF NOT EXISTS reservations (
    reservationID INTEGER PRIMARY KEY,
    memberId INTEGER,
    itemId INTEGER,
    reservationDate DATE NOT NULL,
    status TEXT,
    FOREIGN KEY (itemId) REFERENCES future_item(futureItemId),
    FOREIGN KEY (memberId) REFERENCES member(memberId)
);
```