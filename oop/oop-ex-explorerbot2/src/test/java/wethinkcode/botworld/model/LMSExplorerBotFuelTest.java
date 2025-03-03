package wethinkcode.botworld.model;

import org.hamcrest.Matcher;
import org.junit.jupiter.api.Test;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;
import static org.junit.jupiter.api.Assertions.*;
import static wethinkcode.botworld.model.ExplorerBot.*;
import static wethinkcode.botworld.model.ExplorerBotTest.X_INSIDE;
import static wethinkcode.botworld.model.ExplorerBotTest.Y_INSIDE;
import static wethinkcode.botworld.model.Heading.*;

// Note that we don't need to explicitly test the `setFuelPerKlik` and `getFuelPerKlik` methods:
// they're implicitly tested just by being used in other tests. Don't write unnecessary and
// meaningless tests.
public class LMSExplorerBotFuelTest
{
    public static final Coord INSIDE_THE_WORLD = new Coord( X_INSIDE, Y_INSIDE );
    public static final Coord NORTH_BORDER = new Coord( X_INSIDE, 0 );
    public static final Coord SOUTH_BORDER = new Coord( X_INSIDE, WORLD_MAX_Y );
    public static final Coord WEST_BORDER = new Coord( 0, Y_INSIDE );
    public static final Coord EAST_BORDER = new Coord( WORLD_MAX_X, Y_INSIDE );

    @Test
    void maxFuelIs100(){
        ExplorerBot bot = new ExplorerBot( INSIDE_THE_WORLD, MAX_FUEL );
        bot.addFuel( 1f );
        assertThat( bot.fuelLevel(), equalTo( MAX_FUEL ) );
    }

    @Test
    void minFuelIs0(){
        ExplorerBot bot = new ExplorerBot( INSIDE_THE_WORLD, MIN_FUEL );
        bot.addFuel( -1f );
        assertThat( bot.fuelLevel(), equalTo( 0f ) );
    }

    @Test
    void movingConsumesFuel_LegalMoveN(){
        fuelTest( new ExplorerBot( INSIDE_THE_WORLD, 100f ),
            N,
            lessThan( 100f ));
    }

    @Test
    void movingConsumesFuel_LegalMoveS(){
        fuelTest( new ExplorerBot( INSIDE_THE_WORLD, 100f ),
            S,
            lessThan( 100f ));
    }

    @Test
    void movingConsumesFuel_LegalMoveE(){
        fuelTest( new ExplorerBot( INSIDE_THE_WORLD, 100f ),
            E,
            lessThan( 100f ));
    }

    @Test
    void movingConsumesFuel_LegalMoveW(){
        fuelTest( new ExplorerBot( INSIDE_THE_WORLD, 100f ),
            W,
            lessThan( 100f ));
    }

    @Test
    void movingConsumesFuel_IllegalMoveN(){
        fuelTest( new ExplorerBot( NORTH_BORDER, 100f ),
            N,
            equalTo( 100f ));
    }

    @Test
    void movingConsumesFuel_IllegalMoveS(){
        fuelTest( new ExplorerBot( SOUTH_BORDER, 100f ),
            S,
            equalTo( 100f ));
    }

    @Test
    void movingConsumesFuel_IllegalMoveE(){
        fuelTest( new ExplorerBot( EAST_BORDER, 100f ),
            E,
            equalTo( 100f ));
    }

    @Test
    void movingConsumesFuel_IllegalMoveW(){
        fuelTest( new ExplorerBot( WEST_BORDER, 100f ),
            W,
            equalTo( 100f ));
    }

    @Test
    void turningConsumesNoFuel(){
        ExplorerBot bot = new ExplorerBot( INSIDE_THE_WORLD, 100f );
        bot.turnTo( N );
        bot.turnTo( S );
        bot.turnTo( E );
        bot.turnTo( W );
        assertThat( bot.fuelLevel(), equalTo( 100f ) );
    }

    @Test
    void lowFuelMeansNoMoving(){
        ExplorerBot bot = new ExplorerBot( INSIDE_THE_WORLD, 1f );
        bot.setFuelConsumptionPerKlik( 2f );
        bot.move();
        assertEquals( INSIDE_THE_WORLD, bot.position() );
    }

    private void fuelTest( ExplorerBot aBot, Heading hdg, Matcher<Float> expectation ){
        aBot.turnTo( hdg );
        aBot.move();
        assertThat( aBot.fuelLevel(), expectation );
    }
}
