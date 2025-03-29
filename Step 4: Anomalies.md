# Identifying FD's

## Member Table:
<!-- -Attributes: {memberId (PK), firstName,lastName, dateOfBirth, email, phone, address, membershipStart, membershipEnd} -->
FD: memberID -> firstName, lastName, dateOfBirth, email, phone, address, membershipStart, memebershipEnd
BCNF: No violation since superkey exists.

## Item Table:
FD: itemId -> title, itemType, author, publisher, publicationYear, edition, genre, language, ISBN, availableCopies, totalCopies, location .
BCNF: No violation since superkey exists.

## Personnel Table:
FD: employeeId -> name, position, department, hireDate, contactInfo.
BCNF: No violation since employeeID superkey exists.

## borrow_transaction Table:
FD: transactionId (PK)-> borrowDate, dueDate, returnDate, fineAmount 
BCNF: No violation since transactionId  superkey exists.

## Fine Table
FD: fineId (PK) -> amount, issueDate, paymentDate
BCNF: No violation since fineId superkey exists.

## Event Table
FD: eventId (PK) -> eventName, eventType, description, targetAudience, date, startTime, endTime, roomId (FK)
BCNF:  No violation since eventID determines all other attributes.

## Room Table
FD: roomId (PK) -> roomName, capacity.
BCNF: No violation as roomID determines roomName and capacity.

## future_item Table
FD: futureItemID (PK) -> title, itemType, author, expectedArrivalDate, status.
BCNF: No violation as futureItemID determines all other attributes.

## Reservations Table
FD: reservationID (PK) -> reservationDate, status
BCNF: No violation exists.




