
    $(document).on('change',function(){
        // QUESTION ONE
        $("#exampleSelect1").on('change',function(){
            console.log("In 1");
            
          var selectedValue = $("#exampleSelect1").val();
          if (selectedValue == "Short Answer") 
          {$(".showShortAnswer1").slideDown(500);}
          else{$(".showShortAnswer1").slideUp(500);}

          if (selectedValue == "Multiple Choice") 
          {$(".showMultipleChoice1").slideDown(500);
           $(".showMC1").slideDown(500);
           }
          else{
            $(".showMultipleChoice1").slideUp(500);
            $(".showMC1").slideUp(500);
          }

          if (selectedValue == "True or False") 
          {$(".showTrueFalse1").slideDown(500);}
          else{$(".showTrueFalse1").slideUp(500);}
        }); 
    
        $("#multipleChoice1").on('change',function(){
          var selectedValue = $("#multipleChoice1").val();
          if (selectedValue >= 1) 
          {
            $(".showChoiceOne1").slideDown(500);
            if (selectedValue >= 2) {
              $(".showChoiceTwo1").slideDown(500);
              if (selectedValue >= 3) {
                 $(".showChoiceThree1").slideDown(500);
                 if (selectedValue >= 4) {
                    $(".showChoiceFour1").slideDown(500);
                    if (selectedValue == 5) {
                      $(".showChoiceFive1").slideDown(500);
                    }
                    else {
                      $(".showChoiceFive1").slideUp(500);
                    }
                 }
                 else {
                  $(".showChoiceFour1").slideUp(500);
                 }
               }
               else {
                $(".showChoiceThree1").slideUp(500);
               }
             }
             else {
              $(".showChoiceTwo1").slideUp(500);
             }
          }
          else {
            $(".showChoiceOne1").slideUp(500);
          }
        }); 
    


        // QUESTION TWO
        $("#exampleSelect2").on('change',function(){
            console.log("In 2");
            var selectedValue1 = $("#exampleSelect2").val();
            if (selectedValue1 == "Short Answer") 
            {$(".showShortAnswer2").slideDown(500);}
            else{$(".showShortAnswer2").slideUp(500);}

            if (selectedValue1 == "Multiple Choice") 
            {$(".showMultipleChoice2").slideDown(500);
            $(".showMC1").slideDown(500);}
            else{$(".showMultipleChoice2").slideUp(500);
            $(".showMC2").slideUp(500);
          }

            if (selectedValue1 == "True or False") 
            {$(".showTrueFalse2").slideDown(500);}
            else{$(".showTrueFalse2").slideUp(500);}
          }); 
      
          $("#multipleChoice2").on('change',function(){
            var selectedValue = $("#multipleChoice2").val();
            if (selectedValue >= 1) 
            {
              $(".showChoiceOne2").slideDown(500);
              if (selectedValue >= 2) {
                $(".showChoiceTwo2").slideDown(500);
                if (selectedValue >= 3) {
                   $(".showChoiceThree2").slideDown(500);
                   if (selectedValue >= 4) {
                      $(".showChoiceFour2").slideDown(500);
                      if (selectedValue == 5) {
                        $(".showChoiceFive2").slideDown(500);
                      }
                      else {
                        $(".showChoiceFive2").slideUp(500);
                      }
                   }
                   else {
                    $(".showChoiceFour2").slideUp(500);
                   }
                 }
                 else {
                  $(".showChoiceThree2").slideUp(500);
                 }
               }
               else {
                $(".showChoiceTwo2").slideUp(500);
               }
            }
            else {
              $(".showChoiceOne2").slideUp(500);
            }
          }); 
    
        //   QUESTION THREE
        $("#exampleSelect3").on('change',function(){
            var selectedValue = $("#exampleSelect3").val();
            if (selectedValue == "Short Answer") 
            {$(".showShortAnswer3").slideDown(500);}
            else{$(".showShortAnswer3").slideUp(500);}

            if (selectedValue == "Multiple Choice") 
            {
              $(".showMultipleChoice3").slideDown(500);
              $(".showMC4").slideDown(500);
            }
            else{
              $(".showMultipleChoice3").slideUp(500);
              $(".showMC4").slideUp(500);
            }

            if (selectedValue == "True or False") 
            {$(".showTrueFalse3").slideDown(500);}
            else{$(".showTrueFalse3").slideUp(500);}
          }); 
      
          $("#multipleChoice3").on('change',function(){
            var selectedValue = $("#multipleChoice3").val();
            if (selectedValue >= 1) 
            {
              $(".showChoiceOne3").slideDown(500);
              if (selectedValue >= 2) {
                $(".showChoiceTwo3").slideDown(500);
                if (selectedValue >= 3) {
                   $(".showChoiceThree3").slideDown(500);
                   if (selectedValue >= 4) {
                      $(".showChoiceFour3").slideDown(500);
                      if (selectedValue == 5) {
                        $(".showChoiceFive3").slideDown(500);
                      }
                      else {
                        $(".showChoiceFive3").slideUp(500);
                      }
                   }
                   else {
                    $(".showChoiceFour3").slideUp(500);
                   }
                 }
                 else {
                  $(".showChoiceThree3").slideUp(500);
                 }
               }
               else {
                $(".showChoiceTwo3").slideUp(500);
               }
            }
            else {
              $(".showChoiceOne3").slideUp(500);
            }
          }); 
    
          //QUESTION FOUR
          $("#exampleSelect4").on('change',function(){
            var selectedValue = $("#exampleSelect4").val();
            if (selectedValue == "Short Answer") 
            {$(".showShortAnswer4").slideDown(500);}
            else{$(".showShortAnswer4").slideUp(500);}
          }); 
      
          $("#exampleSelect4").on('change',function(){
            var selectedValue = $("#exampleSelect4").val();
            if (selectedValue == "Multiple Choice") 
            {$(".showMultipleChoice4").slideDown(500);
            $(".showMC4").slideDown(500);
          }
            else{
              $(".showMultipleChoice4").slideUp(500);
            $(".showMC4").slideUp(500);
          }
          }); 
      
          $("#exampleSelect4").on('change',function(){
            var selectedValue = $("#exampleSelect4").val();
            if (selectedValue == "True or False") 
            {$(".showTrueFalse4").slideDown(500);}
            else{$(".showTrueFalse4").slideUp(500);}
          }); 
      
          $("#multipleChoice4").on('change',function(){
            var selectedValue = $("#multipleChoice1").val();
            if (selectedValue >= 1) 
            {
              $(".showChoiceOne4").slideDown(500);
              if (selectedValue >= 2) {
                $(".showChoiceTwo4").slideDown(500);
                if (selectedValue >= 3) {
                   $(".showChoiceThree4").slideDown(500);
                   if (selectedValue >= 4) {
                      $(".showChoiceFour4").slideDown(500);
                      if (selectedValue == 5) {
                        $(".showChoiceFive4").slideDown(500);
                      }
                      else {
                        $(".showChoiceFive4").slideUp(500);
                      }
                   }
                   else {
                    $(".showChoiceFour4").slideUp(500);
                   }
                 }
                 else {
                  $(".showChoiceThree4").slideUp(500);
                 }
               }
               else {
                $(".showChoiceTwo4").slideUp(500);
               }
            }
            else {
              $(".showChoiceOne4").slideUp(500);
            }
          }); 
    
          

       });