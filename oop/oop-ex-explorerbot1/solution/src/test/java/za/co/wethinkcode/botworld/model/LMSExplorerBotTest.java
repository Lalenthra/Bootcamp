package za.co.wethinkcode.botworld.model;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class LMSExplorerBotTest
{
    private static final int MIDDLE_X = ExplorerBot.WORLD_MAX_X / 2;
    private static final int MIDDLE_Y = ExplorerBot.WORLD_MAX_Y / 2;

    @Test
    void moveNorth_insideWorld(){
        ExplorerBot bot =  new ExplorerBot( MIDDLE_X, MIDDLE_Y );
        bot.turnTo( Heading.N );
        bot.move();
        assertEquals( MIDDLE_Y - 1, bot.yPosition() );
    }

    @Test
    void moveSouth_insideWorld(){
        ExplorerBot bot =  new ExplorerBot( MIDDLE_X, MIDDLE_Y );
        bot.turnTo( Heading.S );
        bot.move();
        assertEquals( MIDDLE_Y + 1, bot.yPosition() );
    }

    @Test
    void moveWest_insideWorld(){
        ExplorerBot bot =  new ExplorerBot( MIDDLE_X, MIDDLE_Y );
        bot.turnTo( Heading.W );
        bot.move();
        assertEquals( MIDDLE_X - 1, bot.xPosition() );
    }

    @Test
    void moveEast_insideWorld(){
        ExplorerBot bot =  new ExplorerBot( MIDDLE_X, MIDDLE_Y );
        bot.turnTo( Heading.E );
        bot.move();
        assertEquals( MIDDLE_X + 1, bot.xPosition() );
    }

    @Test
    void moveNorth_outsideWorld(){
        ExplorerBot bot =  new ExplorerBot( MIDDLE_X, 0 );
        bot.turnTo( Heading.N );
        bot.move();
        assertEquals( 0, bot.yPosition() );
    }

    @Test
    void moveSouth_outsideWorld(){
        ExplorerBot bot =  new ExplorerBot( MIDDLE_X, ExplorerBot.WORLD_MAX_Y );
        bot.turnTo( Heading.S );
        bot.move();
        assertEquals( ExplorerBot.WORLD_MAX_Y, bot.yPosition() );
    }

    @Test
    void moveWest_outsideWorld(){
        ExplorerBot bot =  new ExplorerBot( 0, MIDDLE_Y );
        bot.turnTo( Heading.W );
        bot.move();
        assertEquals( 0, bot.xPosition() );
    }

    @Test
    void moveEast_outsideWorld(){
        ExplorerBot bot =  new ExplorerBot( ExplorerBot.WORLD_MAX_X, MIDDLE_Y );
        bot.turnTo( Heading.E );
        bot.move();
        assertEquals( ExplorerBot.WORLD_MAX_X, bot.xPosition() );
    }
}