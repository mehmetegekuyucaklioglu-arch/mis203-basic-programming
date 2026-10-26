# Week 5 Lab: Reusable Shipping Quote

## 📝 Summary
In this lab, we created a modular shopping cart, discount, and shipping calculation program using functions to avoid code duplication.

---

## 🧪 Testing & Changes
- **Test Run:** I tested an order of 2 items priced at 600 TL each for a non-member customer (Subtotal: 1200 TL). The 10% discount and free shipping for orders over 500 TL applied correctly, resulting in a final total of 1080.0 TL.
- **Change Made:** Initially, the shipping fee checked only member status. After testing, I updated it so that orders of 500 TL or more also get free shipping even if the customer is not a member.

---

## 💡 Difference Between `print` and `return`
* **`print()`:** Only displays the result on the screen (console). It does not save the value in memory, meaning you cannot reuse that value in later calculations.
* **`return`:** Sends the calculated result back to the program's memory. This allows you to store the output in variables, pass it into other functions, or use it in further operations.
