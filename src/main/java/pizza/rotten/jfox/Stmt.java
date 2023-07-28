package pizza.rotten.jfox;

abstract class Stmt {

    abstract <R> R accept(Visitor<R> visitor);

    interface Visitor<R> {
        R visitExpressionStmt(Expression expression);
        R visitPrintStmt(Print print);
    }

    static class Expression extends Stmt {
        final Expr expression;

        Expression(Expr expression) {
            this.expression = expression;
        }
        @Override
        <R> R accept(Visitor<R> visitor) {
            return visitor.visitExpressionStmt(this);
        };
    }

    static class Print extends Stmt {
        final Expr expression;

        Print(Expr expression) {
            this.expression = expression;
        }
        @Override
        <R> R accept(Visitor<R> visitor) {
            return visitor.visitPrintStmt(this);
        };
    }

}