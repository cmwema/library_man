# Library Management Web Application

## Overview

This web application is designed to streamline the operations of a local library, providing essential features for efficient library management. The application is specifically tailored for use by librarians, simplifying tasks related to book tracking, member management, and transaction handling.

## Functionalities

### 1. Base Library System

#### 1.1 Books
- Maintain a catalog of books with the ability to track stock levels.
- Perform CRUD operations on books.

#### 1.2 Members
- Manage a list of library members.
- Perform CRUD operations on members.

#### 1.3 Transactions
- Record and manage transactions related to book issuances and returns.
- Implement rent fee charges on book returns.

### 2. Use Cases

#### 2.1 General CRUD Operations
- Librarians can perform Create, Read, Update, and Delete operations on both Books and Members, ensuring an up-to-date and accurate database.

#### 2.2 Book Issuance
- Librarians have the capability to issue books to library members, maintaining a record of books lent out.

#### 2.3 Book Returns
- Librarians can process book returns from members, applying necessary rent fees and updating stock levels.

#### 2.4 Book Search
- A search functionality allows librarians to quickly find books based on name and author, enhancing the efficiency of book retrieval.

#### 2.5 Rent Fee Charging
- The system automatically charges rent fees on book returns, ensuring proper financial tracking and management.

#### 2.6 Debt Limit Control
- Librarians can monitor and enforce a policy where a member's outstanding debt should not exceed KES.500, preventing financial discrepancies.

## Assumptions

- The application assumes a single-user scenario, where the librarian is the sole user interacting with the system.
- Session management and role-based access control are not implemented for simplicity.

## Getting Started

1. Clone this repository.
2. Install the necessary dependencies (list provided in the project documentation).
3. Configure the database settings.
4. Run the application.

## Technologies Used

- Python
- Django
- Bootstrap
- Javascript
- SQLite


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.