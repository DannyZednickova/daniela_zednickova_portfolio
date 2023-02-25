
 <form class="form" method ="POST">
        <input type="text" name="name" placeholder="Kdo nám píše?">
        <input type="email" name="email" placeholder="Máš email? :)">
        <input type="number" name="year" placeholder="Jaký je rok? "> <small>/ antispam</small> <br>

        <textarea name="text-email" cols="80" rows="10" placeholder=" Copak bys rád věděl? :) Děkujeme! "></textarea><br>
            <input class="submit" type="submit" value="odeslat">
    </form>


<form  method="post" class="wpcf7-form" >
	<p><label> Vaše jméno (vyžadováno)<br>
		<span class="wpcf7-form-control-wrap your-name"><input type="text" name="name"  size="40" class="wpcf7-form-control wpcf7-text wpcf7-validates-as-required" aria-required="true" aria-invalid="false"></span> </label></p>
	<p><label> Váš e-mail (vyžadováno)<br>
		<span class="wpcf7-form-control-wrap your-email"><input type="email" name="email" size="40" class="wpcf7-form-control wpcf7-text wpcf7-email wpcf7-validates-as-required wpcf7-validates-as-email" aria-required="true" aria-invalid="false"></span> </label></p>
	<p><label> Telefon <br>
		<span class="wpcf7-form-control-wrap your-subject"><input type="tel" name="tel" size="40" class="wpcf7-form-control wpcf7-text" ></span> </label></p>
		<p><label> Jaký je rok? <br>
		<span class="wpcf7-form-control-wrap your-subject"><input type="number" name="year" size="40" class="wpcf7-form-control wpcf7-text" ></span> </label></p>

	<p><label> Vaše zpráva<br>
		<span class="wpcf7-form-control-wrap your-message"><textarea name="text-email"  cols="40" rows="10" class="wpcf7-form-control wpcf7-textarea" aria-invalid="false"></textarea></span> </label></p>
	<p> <input class="submit" type="submit" value="odeslat"></p>
</form>

