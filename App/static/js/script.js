window.onload = function () {
  const creditButton = document.querySelector(".creditbutton");
  const debitButton = document.querySelector(".debitbutton");
  const amountInput = document.querySelector("input[name='amount']");
  const descriptionInput = document.querySelector("input[name='description']");
  const dateInput = document.querySelector("input[type='date']");
  const balance = document.querySelector(".balance");
  const logoutButton = document.querySelector(".logoutbutton");
  const deleteButtons = document.querySelectorAll(".deletebutton");

  // Add event listener to the logout button
  logoutButton.addEventListener("click", function () {
    window.location.href = "/logout";
  });

  // Add event listeners to the buttons
  creditButton.addEventListener("click", async function () {
    // Get the data from the inputs
    const amount = amountInput.value;
    const description = descriptionInput.value;
    const date = dateInput.value;

    // Make a POST request to the API
    const response = await fetch("/api/transactions/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        amount,
        description,
        date,
        type: "credit",
      }),
    });

    // Get the updated data from the API
    const transactionsResponse = await response.json();
    // Convert the transactions object to an array
    const transactions = Array.from(transactionsResponse);
    if (!Array.isArray(transactions)) {
      throw new TypeError("transactions is not an array");
    }

    const total = transactions.reduce((acc, curr) => {
      return acc + curr.amount;
    }, 0);
    console.log(total);

    // Update the balance on the frontend
    const balance = transactions.reduce((total, transaction) => {
      if (transaction.type === "credit") {
        return total + transaction.amount;
      } else {
        return total - transaction.amount;
      }
    }, 0);
    document.querySelector(".balance").innerHTML = "Balance: $" + balance;
  });

  debitButton.addEventListener("click", async function () {
    // Get the data from the inputs
    const amount = amountInput.value;
    const description = descriptionInput.value;
    const date = dateInput.value;

    // Make a POST request to the API
    const response = await fetch("/api/transactions/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        amount,
        description,
        date,
        type: "debit",
      }),
    });

    // Get the updated data from the API
    const transactions = await response.json();

    // Update the balance on the frontend
    const balance = transactions.reduce((total, transaction) => {
      if (transaction.type === "credit") {
        return total + transaction.amount;
      } else {
        return total - transaction.amount;
      }
    }, 0);
    document.querySelector(".balance").innerHTML = "Balance: $" + balance;
  });
  deleteButtons.forEach(function (deleteButton) {
    deleteButton.addEventListener("click", function (event) {
      event.preventDefault();

      const transactionId = event.target.getAttribute("href").split("/").pop();

      fetch(`http://localhost:8000/transactions/${transactionId}/`, {
        method: "DELETE",
      })
        .then((response) => {
          if (response.ok) {
            return response.json();
          }
          throw new Error("Network response was not ok");
        })
        .then((data) => {
          console.log("Transaction deleted successfully: ", data);
          const parentRow = event.target.closest("tr");
          parentRow.remove();
        })
        .catch((error) => {
          console.error(
            "There was a problem with the fetch operation: ",
            error
          );
        });
    });
  });
};
