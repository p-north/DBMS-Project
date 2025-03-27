## Step 2: Project Specifications (10 Points)

	member = {memberId (PK), firstName,lastName, dateOfBirth, email, phone, address, membershipStart, membershipEnd}

	item = { itemId (PK) , title, itemType, author, publisher, publicationYear, edition, genre, language, ISBN, availableCopies, totalCopies, location }

	personnel = {employeeId, name, position, department, hireDate, contactInfo}
	
	borrow_transaction = { transactionId (PK), memberId (FK), itemId (FK), borrowDate, dueDate, returnDate, fineAmount }
	
	fine = { fineId (PK), memberId (FK), transactionId (FK), amount, issueDate, paymentDate }

	event = { eventId (PK), eventName, eventType, description, targetAudience, date, startTime, endTime, roomId (FK) }

	room = {roomId (PK), roomName, capacity}

	future_item = {futureItemId (PK), title, itemType, author, expectedArrivalDate, status}

	reservations = { reservationID (PK), memberId (FK), itemId (FK), reservationDate, status}

## Relationships:

**member -> borrow_transaction**

A member can have multiple borrow transactions, but each only to one member meaning that this is a one-to-many

**item -> borrow_transaction**

An item can be borrowed multiple times, but each transaction is only for one item. Meaning this is a one-to-many

**borrow_transaction -> fine**

A transaction may result in a fine but a fine is only for one transaction. Meaning this is a one to many

**member -> fine**

A member can place multiple reservations, but each reservation is only for one of the members. Meaning this is a one to many.

**member -> reservations**

A member can place multiple reservations,but each reservation is only for one member.. Meaning this is a one to many

**item -> reservations**

An item can be reserved multiple times, but each reservation is only for one item. Meaning this is a one to many

**room -> event**

A room can host multiple events, but each event is in one room.

**personnel -> event**

Personnel organize events, but this isn’t explicitly modeled. Meaning this is indirect.
