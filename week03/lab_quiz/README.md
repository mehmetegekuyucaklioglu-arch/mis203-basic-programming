Week 3 Lab: Order Approval Policy

This program implements an order approval policy that evaluates order inputs (amount, stock, requested quantity, and membership status) to determine approval, discount application, and final price calculation.

Test Table 

Test Case | Order Amount (TRY) | Available Stock | Requested Quantity | Is Member | Expected Result | Reason for Output |

Below Threshold | 499.00 | 10 | 2 | Yes | Approved (499.00 TRY) | Amount is below 500 TRY, no discount applied. |
Exact Threshold | 500.00 | 10 | 2 | Yes | Approved (450.00 TRY) | Exact boundary: 10% member discount applied ($500 - 10\% = 450$). |
Above Threshold | 501.00 | 10 | 2 | Yes | Approved (450.90 TRY) | Amount is above 500 TRY, 10% member discount applied. |
Insufficient Stock | 600.00 | 5 | 10 | Yes | Rejected | Requested quantity exceeds available stock (No price shown). |
Invalid Quantity  | 500.00 | 10 | 0 | Yes | Rejected | Quantity must be greater than zero (No price shown). |


Test and  Change Note

Test Executed: Tested boundary cases for member discount at `499 TRY`, `500 TRY`, and `501 TRY`.
Change Made: Updated the discount condition from `order_amount > 500` to `order_amount >= 500` to ensure customers buying at exactly `500 TRY` correctly receive the 10% discount.
