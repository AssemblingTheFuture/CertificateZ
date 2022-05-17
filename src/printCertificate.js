var doc = new jsPDF();

var specialElementHandlers = {
    '#editor': function (element, renderer) {
        return true;
    }
};

$('#generatePDF').click(function () {
    doc.fromHTML($('#content').html(), 15, 15, {
        'width': 170,
            'elementHandlers': specialElementHandlers
    });
    doc.save('Certificate.pdf');
});
