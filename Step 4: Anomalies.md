# Identifying FD's

## Member Table:
<!-- -Attributes: {memberId (PK), firstName,lastName, dateOfBirth, email, phone, address, membershipStart, membershipEnd} -->
FD: memberID -> firstName, lastName, dateOfBirth, email, phone, address, membershipStart, memebershipEnd
BCNF: No violation since superkey exists.

## Item Table:
FD: itemId -> title, itemType, author, publisher, publicationYear, edition, genre, language, ISBN, availableCopies, totalCopies, location .
BCNF: No violation since superkey exists.

