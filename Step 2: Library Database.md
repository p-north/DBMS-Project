## Step 2: Project Specifications (10 Points)

	member = {memberId, firstName,lastName, dateOfBirth, email, phone, address, membershipStart, membershipEnd}

	item = { itemId, title, itemType, author, publisher, publicationYear, edition, genre, language, ISBN, availableCopies, totalCopies, location }

	personnel = {employeeId, name, position, department, hireDate, contactInfo}
	
	borrow_transaction = { transactionId, memberId, itemId, borrowDate, dueDate, returnDate, fineAmount }
	
	fine = { fineId, memberId, transactionId, amount, issueDate, paymentDate }

	event = { eventId, eventName, eventType, description, targetAudience, date, startTime, endTime, roomId }

	room = {roomId, roomName, capacity}

	future_item = {futureItemId, title, itemType, author, expectedArrivalDate, status}

	reservations = { reservation, memberId, itemId, reservationDate, status}

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
