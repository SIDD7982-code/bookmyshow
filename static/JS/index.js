$(function () {

    $(".movie-category a").click(function () {

        //var category = $(this).attr("href");

        $(".movie-category a").removeClass("active");
        $(this).addClass("active");

        // $.ajax({
        //     url: category,
        //     success: function(data){
        //         $(".movie-list").html(data);
        //     }
        // });


    });

    let seat_layout = `
                    <div class="row my-2">
                        <div class="col-1" >
                            <h6 class="text-muted" id="seat_row">O</h6>
                        </div>
                        <div class="col-5" id="seat_col-1">
                            <div class="container">
                                all_row_layout_1
                            </div>
                        </div>
                        <div class="col-5" id="seat_col-2">
                            <div class="container">
                                all_row_layout_2
                            </div>
                        </div>

</div>
`

    let seat = `
            <div class="col-1">
                <input type="checkbox" class="btn-check seat" id="seat_no"  name="seat" value="seat_no">
                <label class="btn btn-outline-primary" for="seat_no"> seat_number </label>
            </div>
        
    `

    let seat_row = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
    seat_row.reverse()

    for (row of seat_row) {
        let seat_layout_copy= seat_layout
        seat_layout_copy = seat_layout_copy.replace("O", row)

        let seat_copy= seat
        let all_seat_html = ""

        for (let i = 1; i <=9; i++) {
            let seat_no = row + i
            seat_copy= seat
            seat_copy = seat_copy.replaceAll("seat_no", seat_no)
            seat_copy = seat_copy.replace("seat_number", i)
            all_seat_html += seat_copy
        }

        let seat_row= `
        <div class="row" id="seat_row_layout_1">
          ${all_seat_html}      
        </div>`

        seat_layout_copy = seat_layout_copy.replace("all_row_layout_1", seat_row)
//        reserved_seat= document.getElementById("all_reserverd_seats").textContent
//        console.log("Reserverd Seats")
//        console.log(reserved_seat)
//        console.log(reserved_seat.split(" "))


        all_seat_html = ""
        for (let i = 10; i <=18; i++) {
            let seat_no = row + i
            seat_copy= seat

            seat_copy = seat_copy.replaceAll("seat_no", seat_no)
            seat_copy = seat_copy.replace("seat_number", i)
            all_seat_html += seat_copy
        }

        seat_row= `
        <div class="row gx-5" id="seat_row_layout_2">
          ${all_seat_html}      
        </div>`

        seat_layout_copy = seat_layout_copy.replace("all_row_layout_2", seat_row)
        document.getElementById("seat_layout").innerHTML += seat_layout_copy

    }

    $(".seat").click(function () {
        if ($(this).is(":checked")) {
            $(this).addClass("selected")
        } else {
            $(this).removeClass("selected")
        }

       $(".price").text(200*$(".selected").length)

       $("#total-price")[0].value= 200*$(".selected").length;


    });

    all_reserverd_seats= $("#reserved_seats")[0].innerHTML
    reserved_seat_array= JSON.parse(all_reserverd_seats)
    reserved_seat_array.forEach( seat_obj =>{
        seat= document.getElementById(`${seat_obj["seat"]}`)
        seat.disabled= true
        seat.nextElementSibling.classList.remove('btn-outline-primary')
        seat.nextElementSibling.classList.add('btn-secondary')

    })

});