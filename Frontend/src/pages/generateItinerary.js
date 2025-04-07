import jsPDF from "jspdf";
import html2canvas from "html2canvas";

const generatePDF = () => {
    const itineraryElement = document.getElementById("itinerary-content");

    if (!itineraryElement) {
        alert("❌ No itinerary content found!");
        return;
    }

    html2canvas(itineraryElement, {
        scale: 2, // High quality
        useCORS: true, // Support external images
        backgroundColor: null, // Transparent background
        logging: false,
    }).then((canvas) => {
        const pdf = new jsPDF("p", "mm", "a4");
        const imgWidth = 190; // A4 width
        const pageHeight = 297; // A4 height in mm
        const imgHeight = (canvas.height * imgWidth) / canvas.width;
        let heightLeft = imgHeight;
        let position = 10;

        pdf.addImage(canvas.toDataURL("image/png"), "PNG", 10, position, imgWidth, imgHeight);
        heightLeft -= pageHeight;

        while (heightLeft > 0) {
            position -= pageHeight;
            pdf.addPage();
            pdf.addImage(canvas.toDataURL("image/png"), "PNG", 10, position, imgWidth, imgHeight);
            heightLeft -= pageHeight;
        }

        pdf.save("Itinerary.pdf");
    }).catch((error) => {
        console.error("❌ PDF Generation Error:", error);
        alert("Failed to generate PDF!");
    });
};

export default generatePDF;
