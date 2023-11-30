# Library Access Control Project

## Summary
Implementing RBAC Model to the library website. The role of the user determines what actions they can perform within the website.

This model uses RBAC (Role-Based Access Control) Model, involving password encryption using hash. Storing user data using SQLAlchemy. The Website mimics a library site where different user have different access to the website, such as check-out books, add/delete books to the book database, add/remove users to the system.

## Use Case
1. Signup
2. Login
3. Delete users - admins only
4. Add books - librarians only
5. Checkout - users only
6. View database - admins only
7. Guests

## Usage
The OS or terminal must support flask and wtforms.

## Installation
pip install flask
