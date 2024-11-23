document.addEventListener("DOMContentLoaded", function () {
    const dashboardContent = document.getElementById("dashboard-content");
    const assignmentsContent = document.getElementById("assignments-content");
    const gradesContent = document.getElementById("grades-content");
    const scheduleContent = document.getElementById("schedule-content");
    const messagesContent = document.getElementById("messages-content");
  
    const links = document.querySelectorAll(".sidebar a");
  
    function showContent(content) {
      // Hide all contents first
      const allContents = document.querySelectorAll(".content");
      allContents.forEach((contentElement) => {
        contentElement.style.display = "none";
      });
  
      // Show selected content
      content.style.display = "block";
    }
  
    // Initial content display
    showContent(dashboardContent);
  
    // Event listeners for the sidebar links
    links.forEach((link) => {
      link.addEventListener("click", function (event) {
        event.preventDefault();
  
        // Change the content based on the clicked link
        if (link.id === "dashboard") {
          showContent(dashboardContent);
        } else if (link.id === "assignments") {
          showContent(assignmentsContent);
        } else if (link.id === "grades") {
          showContent(gradesContent);
        } else if (link.id === "schedule") {
          showContent(scheduleContent);
        } else if (link.id === "messages") {
          showContent(messagesContent);
        }
      });
    });
  });
  